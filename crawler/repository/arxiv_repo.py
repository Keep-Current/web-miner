import urllib.request
import feedparser
import json

from crawler.domain import arxiv_document as ad

class ArxivRepo:
    """
    This is a helper class to parse arxiv.org site.
    It uses the arxiv.org REST API to search for articles.

    based on karpathy's arxiv-sanity:
    https://github.com/karpathy/arxiv-sanity-preserver/blob/master/fetch_papers.py
    and arxiv example:
    https://arxiv.org/help/api/examples/python_arXiv_parsing_example.txt
    """
        
    # Base api query url
    base_url = 'http://export.arxiv.org/api/query?'

    # Opensearch metadata such as totalResults, startIndex,
    # and itemsPerPage live in the opensearch namespase.
    # Some entry metadata lives in the arXiv namespace.
    # This is a hack to expose both of these namespaces in
    # feedparser v4.1
    feedparser._FeedParserMixin.namespaces['http://a9.com/-/spec/opensearch/1.1/'] = 'opensearch'
    feedparser._FeedParserMixin.namespaces['http://arxiv.org/schemas/atom'] = 'arxiv'
            
    def _check(self, element, key, value):
        if '__' not in key:
            key = key + '__eq'

        key, operator = key.split('__')

        if operator not in ['eq', 'lt', 'gt']:
            raise ValueError('Operator {} is not supported'.format(operator))

        operator = '__{}__'.format(operator)

        return getattr(element[key], operator)(value)

    def list(self, filters=None):
        if not filters:
            return self.fetch_papers()

        # for key, value in filters.items():
        #    result = [e for e in result if self._check(e, key, value)]

        # return [ad.ArxivDocument.from_dict(r) for r in result]

    def encode_feedparser_dict(self, fp_dict):
        """
        recursive function to convert the internal feedparse object to a simple dict
        """
        if isinstance(fp_dict, feedparser.FeedParserDict) or isinstance(fp_dict, dict):
            ret_dict = {}
            for key in fp_dict.keys():
                ret_dict[key] = self.encode_feedparser_dict(fp_dict[key])
            return ret_dict
        elif isinstance(fp_dict, list):
            dict_list = []
            for key in fp_dict:
                dict_list.append(self.encode_feedparser_dict(key))
            return dict_list
        else:
            return fp_dict
        
    def extract_relevant_info(self, fp_dict):
        ret_dict = {}
        ret_dict['publish_date'] = fp_dict['published']
        ret_dict['authors'] = [auth['name'] for auth in fp_dict['authors']]
        ret_dict['title'] = fp_dict['title']
        ret_dict['abstract'] = fp_dict['summary']
        ret_dict['id'] = fp_dict['id'] # may be redundant when guidislink == true
        ret_dict['link'] = fp_dict['link'] 
        
        for link in fp_dict['links']:
            try:
                if link.title == 'pdf':
                    ret_dict['pdf'] = link.href
            except AttributeError:
                pass
                    
        return ret_dict

    def run_query(self, search_query, start=0, max_results=10):
        query = 'search_query=%s&sortBy=lastUpdatedDate&start=%i&max_results=%i' % (search_query,
                                                                                    start,
                                                                                    max_results)
        with urllib.request.urlopen(self.base_url+query) as url:
            response = url.read()
        parsed_response = feedparser.parse(response)

        return parsed_response

    def parse_arxiv_url(self, url):
        """ 
        extracts the raw id and the version
        examples is http://arxiv.org/abs/1512.08756v2
        """
        ix = url.rfind('/')
        idversion = url[ix+1:] # extract just the id (and the version)
        parts = idversion.split('v')
        assert len(parts) == 2, 'error parsing url ' + url
        return parts[0], int(parts[1])

    def fetch_papers(
            self,
            search_query='cat:cs.CV+OR+cat:cs.AI+OR+cat:cs.LG+OR+cat:cs.CL+OR+cat:cs.NE+OR+cat:stat.ML',
            start_index=0,
            max_index=100,
            results_per_iteration=100,
            wait_time=5.0,
            break_on_no_added=True
        ):
        """loops according to the results_per_iteration and fetch results pages from arxiv.org

        Keyword Arguments:
            search_query {str} -- [arxiv.org topics to query] (default: {'cat:cs.CV+OR+cat:cs.AI+OR+cat:cs.LG+OR+cat:cs.CL+OR+cat:cs.NE+OR+cat:stat.ML'})
            start_index {int} -- [pagination start index] (default: {0})
            max_index {int} -- [upper bound on paper index we will fetch] (default: {10000})
            results_per_iteration {int} -- [passed to arxiv API] (default: {100})
            wait_time {float} -- [pause in seconds between requests] (default: {5.0})
            break_on_no_added {bool} -- [break out early if all returned query papers are already in db] (default: {True})
        """
        # num_added_total = 0
        for i in range(start_index, max_index, results_per_iteration):
            print("Results %i - %i" % (i, i+results_per_iteration))

            parsed_response = self.run_query(search_query, i, results_per_iteration)

            results = []

            for entry in parsed_response.entries:
                # print(json.dumps(entry, indent=4))
                # dict_entry = encode_feedparser_dict(entry)
                dict_entry = self.extract_relevant_info(entry)

                rawid, version = self.parse_arxiv_url(dict_entry['link'])
                dict_entry['_rawid'] = rawid
                dict_entry['_version'] = version

                # dict_entry['title']
                # dict_entry['published']
                # dict_entry['author']
                # dict_entry['term'] # categories
                # dict_entry['links'] # PDF
                # dict_entry['summary'] #abstract

                #print(json.dumps(dict_entry, indent=4))
                #print('-----------------------------------------------')

                results.append(dict_entry)
                
        return results

