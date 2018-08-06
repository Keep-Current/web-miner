import uuid
from webminer.entities import arxiv_document as ad

test_url = "https://arxiv.org/abs/1801.06605"
test_title = "A Collaborative Filtering Recommender System"
test_abstract = "The use of relevant metrics of software systems could improve various software engineering tasks, but"
test_authors = ["Maral Azizi", "Hyunsook Do"]
test_publish_date = "Sat, 20 Jan 2018 00:11:42"
test_pdf_url = "https://arxiv.org/pdf/1801.06605"


def test_arxivDoc_model_init():
    code = uuid.uuid4()
    arxivDoc = ad.ArxivDocument(
        doc_id=code,
        url=test_url,
        title=test_title,
        abstract=test_abstract,
        authors=test_authors,
        publish_date=test_publish_date,
        pdf_url=test_pdf_url,
    )
    assert arxivDoc.doc_id == code
    assert arxivDoc.url == test_url
    assert arxivDoc.title == test_title
    assert arxivDoc.abstract == test_abstract
    assert arxivDoc.authors == test_authors
    assert arxivDoc.publish_date == test_publish_date
    assert arxivDoc.pdf_url == test_pdf_url


def test_arxivDoc_model_from_dict():
    code = uuid.uuid4()
    arxivDoc = ad.ArxivDocument.from_dict(
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
    assert arxivDoc.doc_id == code
    assert arxivDoc.url == test_url
    assert arxivDoc.title == test_title
    assert arxivDoc.abstract == test_abstract
    assert arxivDoc.authors == test_authors
    assert arxivDoc.publish_date == test_publish_date
    assert arxivDoc.pdf_url == test_pdf_url
