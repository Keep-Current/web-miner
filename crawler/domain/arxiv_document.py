from crawler.shared.domain_model import DomainModel

class ArxivDocument(object):
    def __init__(
            self, 
            id, 
            title,
            abstract,
            authors,
            url,
            publish_date,
            pdf_url
        ):
        self.id = id
        self.title = title
        self.abstract = abstract
        self.authors = authors
        self.url = url
        self.publish_date = publish_date
        self.pdf_url = pdf_url

    @classmethod
    def from_dict(cls, feedparser_dict):
        pdf = ''
        for link in feedparser_dict['links']:
            try:
                if link['title'] == 'pdf':
                    pdf = link['href']
            except AttributeError:
                pass

        document = ArxivDocument(
            id = feedparser_dict['id'],
            title = feedparser_dict['title'],
            abstract = feedparser_dict['summary'],
            authors = [auth['name'] for auth in feedparser_dict['authors']],
            url = feedparser_dict['url'],
            publish_date = feedparser_dict['published'],
            pdf_url = pdf
        )

        return document

    

DomainModel.register(ArxivDocument)