"""Tests the arxiv model
"""

import uuid
from webminer.entities import arxiv_document as ad

test_url = "https://arxiv.org/abs/1801.06605"
test_title = "A Collaborative Filtering Recommender System"
test_abstract = "The use of relevant metrics of software systems " + \
 "could improve various software engineering tasks, but"
test_authors = ["Maral Azizi", "Hyunsook Do"]
test_publish_date = "Sat, 20 Jan 2018 00:11:42"
test_pdf_url = "https://arxiv.org/pdf/1801.06605"


def test_arxiv_doc_model_init():
    """Tests a successful creation of a arxiv doc model
    """

    code = uuid.uuid4()
    arxiv_doc = ad.ArxivDocument(
        doc_id=code,
        url=test_url,
        title=test_title,
        abstract=test_abstract,
        authors=test_authors,
        publish_date=test_publish_date,
        pdf_url=test_pdf_url,
    )
    assert_equal(arxiv_doc.doc_id, code)
    assert_equal(arxiv_doc.url, test_url)
    assert_equal(arxiv_doc.title, test_title)
    assert_equal(arxiv_doc.abstract, test_abstract)
    assert_equal(arxiv_doc.authors, test_authors)
    assert_equal(arxiv_doc.publish_date, test_publish_date)
    assert_equal(arxiv_doc.pdf_url, test_pdf_url)


def test_arxiv_doc_model_from_dict():
    """Tests a successful creation of a arxiv doc model from a
    dictionary object
    """
    code = uuid.uuid4()
    arxiv_doc = ad.ArxivDocument.from_dict(
        {
            "doc_id": code,
            "url": test_url,
            "title": test_title,
            "summary": test_abstract,
            "authors": [{"name": "Maral Azizi"}, {"name": "Hyunsook Do"}],
            "published": test_publish_date,
            "links": [{"title": "pdf", "href": "https://arxiv.org/pdf/1801.06605"}],
        }
    )
    assert_equal(arxiv_doc.doc_id, code)
    assert_equal(arxiv_doc.url, test_url)
    assert_equal(arxiv_doc.title, test_title)
    assert_equal(arxiv_doc.abstract, test_abstract)
    assert_equal(arxiv_doc.authors, test_authors)
    assert_equal(arxiv_doc.publish_date, test_publish_date)
    assert_equal(arxiv_doc.pdf_url, test_pdf_url)

def assert_equal(arg1, arg2):
    if arg1 != arg2:
        raise AssertionError("Assert equal failed - values are not equal")
