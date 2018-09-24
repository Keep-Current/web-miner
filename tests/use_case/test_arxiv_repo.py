"""Tests the arxiv repository
"""

import pytest
import responses

from webminer.entities.arxiv_document import ArxivDocument
from webminer.use_cases.request_arxiv import arxiv_repo as a_repo

arxiv_doc_1 = ArxivDocument(
    doc_id="url_1",
    url="url_1",
    title="title_1",
    abstract="abstract_1",
    authors=["author1", "author2"],
    publish_date="publish_date_1",
    pdf_url="pfg_url1",
)

arxiv_doc_2 = ArxivDocument(
    doc_id="url_2",
    url="url_2",
    title="title_2",
    abstract="abstract_2",
    authors=["author2", "author2"],
    publish_date="publish_date_2",
    pdf_url="pfg_url2",
)

arxiv_doc_3 = ArxivDocument(
    doc_id="url_3",
    url="url_3",
    title="title_3",
    abstract="abstract_3",
    authors=["author3", "author2"],
    publish_date="publish_date_3",
    pdf_url="pfg_url3",
)

arxiv_doc_4 = ArxivDocument(
    doc_id="url_4",
    url="url_4",
    title="title_4",
    abstract="abstract_4",
    authors=["author4", "author2"],
    publish_date="publish_date_4",
    pdf_url="pfg_url4",
)

arxiv_response = """<?xml version="1.0" encoding="UTF-8"?>
<feed xmlns="http://www.w3.org/2005/Atom">
  <link href="http://arxiv.org/api/query?search_query%3Dcat%3Acs.CV%20OR%20cat%3Acs.AI%20OR%20cat%3Acs.LG%20OR%20cat%3Acs.CL%20OR%20cat%3Acs.NE%20OR%20cat%3Astat.ML%26id_list%3D%26start%3D1%26max_results%3D100" rel="self" type="application/atom+xml"/>
  <title type="html">ArXiv Query: search_query=cat:cs.CV OR cat:cs.AI OR cat:cs.LG OR cat:cs.CL OR cat:cs.NE OR cat:stat.ML&amp;id_list=&amp;start=1&amp;max_results=100</title>
  <id>http://arxiv.org/api//mx7Y+oW1RP05QqmCZfHNto2duM</id>
  <updated>2018-09-23T00:00:00-04:00</updated>
  <opensearch:totalResults xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/">68000</opensearch:totalResults>
  <opensearch:startIndex xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/">1</opensearch:startIndex>
  <opensearch:itemsPerPage xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/">100</opensearch:itemsPerPage>
  <entry>
    <id>http://arxiv.org/abs/1809.07759v1</id>
    <updated>2018-09-20T17:48:27Z</updated>
    <published>2018-09-20T17:48:27Z</published>
    <title>Implementing Adaptive Separable Convolution for Video Frame
  Interpolation</title>
    <summary>  As Deep Neural Networks are becoming more popular, much of the attention is
being devoted to Computer Vision problems that used to be solved with more
traditional approaches.
</summary>
    <author>
      <name>Mart Kartašev</name>
    </author>
    <author>
      <name>Carlo Rapisarda</name>
    </author>
    <author>
      <name>Dominik Fay</name>
    </author>
    <arxiv:comment xmlns:arxiv="http://arxiv.org/schemas/atom">All authors contributed equally</arxiv:comment>
    <link href="http://arxiv.org/abs/1809.07759v1" rel="alternate" type="text/html"/>
    <link title="pdf" href="http://arxiv.org/pdf/1809.07759v1" rel="related" type="application/pdf"/>
    <arxiv:primary_category xmlns:arxiv="http://arxiv.org/schemas/atom" term="cs.CV" scheme="http://arxiv.org/schemas/atom"/>
    <category term="cs.CV" scheme="http://arxiv.org/schemas/atom"/>
  </entry>
  <entry>
    <id>http://arxiv.org/abs/1806.01482v2</id>
    <updated>2018-09-20T17:42:42Z</updated>
    <published>2018-06-05T03:49:46Z</published>
    <title>SoPhie: An Attentive GAN for Predicting Paths Compliant to Social and
  Physical Constraints</title>
    <summary>  This paper addresses the problem of path prediction for multiple interacting
agents in a scene, which is a crucial step for many autonomous platforms such
as self-driving cars and social robots.
</summary>
    <author>
      <name>Amir Sadeghian</name>
    </author>
    <author>
      <name>Vineet Kosaraju</name>
    </author>
    <author>
      <name>Ali Sadeghian</name>
    </author>
    <author>
      <name>Noriaki Hirose</name>
    </author>
    <author>
      <name>S. Hamid Rezatofighi</name>
    </author>
    <author>
      <name>Silvio Savarese</name>
    </author>
    <link href="http://arxiv.org/abs/1806.01482v2" rel="alternate" type="text/html"/>
    <link title="pdf" href="http://arxiv.org/pdf/1806.01482v2" rel="related" type="application/pdf"/>
    <arxiv:primary_category xmlns:arxiv="http://arxiv.org/schemas/atom" term="cs.CV" scheme="http://arxiv.org/schemas/atom"/>
    <category term="cs.CV" scheme="http://arxiv.org/schemas/atom"/>
  </entry>"""

arxiv_result = [
    {
        "publish_date": "2018-09-20T17:48:27Z",
        "authors": ["Mart KartaÅ¡ev", "Carlo Rapisarda", "Dominik Fay"],
        "title": "Implementing Adaptive Separable Convolution for Video Frame\n  Interpolation",
        "abstract": "As Deep Neural Networks are becoming more popular, much of the attention is\nbeing devoted to Computer Vision problems that used to be solved with more\ntraditional approaches.",
        "id": "http://arxiv.org/abs/1809.07759v1",
        "link": "http://arxiv.org/abs/1809.07759v1",
        "pdf": "http://arxiv.org/pdf/1809.07759v1",
        "_rawid": "1809.07759",
        "_version": 1,
    },
    {
        "publish_date": "2018-06-05T03:49:46Z",
        "authors": [
            "Amir Sadeghian",
            "Vineet Kosaraju",
            "Ali Sadeghian",
            "Noriaki Hirose",
            "S. Hamid Rezatofighi",
            "Silvio Savarese",
        ],
        "title": "SoPhie: An Attentive GAN for Predicting Paths Compliant to Social and\n  Physical Constraints",
        "abstract": "This paper addresses the problem of path prediction for multiple interacting\nagents in a scene, which is a crucial step for many autonomous platforms such\nas self-driving cars and social robots.",
        "id": "http://arxiv.org/abs/1806.01482v2",
        "link": "http://arxiv.org/abs/1806.01482v2",
        "pdf": "http://arxiv.org/pdf/1806.01482v2",
        "_rawid": "1806.01482",
        "_version": 2,
    },
]


@pytest.fixture
def domain_arxivdocs():
    """Creates a fixture for the returned objects
    """
    return [arxiv_doc_1, arxiv_doc_2, arxiv_doc_3, arxiv_doc_4]


def assert_equal(arg1, arg2):
    if arg1 != arg2:
        print("arg1: ", arg1)
        print("arg2: ", arg1)
        raise AssertionError("Assert equal failed - values are not equal")


def _check_results(domain_models_list, data_list):
    assert_equal(len(domain_models_list), len(data_list))
    if not all([isinstance(dm, DomainModel) for dm in domain_models_list]):
        raise AssertionError("not all domain model returned true")
    assert_equal(
        set([dm.doc_id for dm in domain_models_list]),
        set([d["doc_id"] for d in data_list]),
    )


def test_repository_list_without_parameters(domain_arxivdocs):
    repo = a_repo.ArxivRepo(domain_arxivdocs)

    assert_equal(repo.list(), domain_arxivdocs)


@responses.activate
def test_extract_relevant_info():
    url = "http://export.arxiv.org/api/query?search_query=cat:cs.CV+OR+cat:cs.AI+OR+cat:cs.LG+OR+cat:cs.CL+OR+cat:cs.NE+OR+cat:stat.ML&sortBy=lastUpdatedDate&start=0&max_results=100"
    responses.add(method=responses.GET, url=url, body=arxiv_response, status=200)

    repo = a_repo.ArxivRepo()
    result = repo.fetch_papers()

    assert_equal(len(result), 2)
    assert_equal(result, arxiv_result)
