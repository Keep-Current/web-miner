import datetime
import json
import pytest

from webminer.serializers.json import arxiv_document_serializer as srs
from webminer.domain.arxiv_document import ArxivDocument

test_url = 'https://arxiv.org/abs/1801.06605'
test_title = 'A Collaborative Filtering Recommender System'
test_abstract = 'The use of relevant metrics of software systems could improve various software engineering tasks, but'
test_authors = ['Maral Azizi', 'Hyunsook Do']
test_publish_date = 'Sat, 20 Jan 2018 00:11:42'
test_pdf_url = 'https://arxiv.org/pdf/1801.06605'


def test_serialize_domain_arxiv_document():
    arxiv_doc = ArxivDocument(
        doc_id = 'f853578c-fc0f-4e65-81b8-566c5dffa35a',
        url= test_url,
        title = test_title,
        abstract = test_abstract,
        authors = test_authors,
        publish_date = test_publish_date,
        pdf_url = test_pdf_url
        )

    expected_json = """
        {
            "id" : "f853578c-fc0f-4e65-81b8-566c5dffa35a",
            "url" : "https://arxiv.org/abs/1801.06605",
            "title" : "A Collaborative Filtering Recommender System",
            "abstract" : "The use of relevant metrics of software systems could improve various software engineering tasks, but",
            "authors" : "Maral Azizi,Hyunsook Do",
            "publish_date" : "Sat, 20 Jan 2018 00:11:42",
            "pdf" : "https://arxiv.org/pdf/1801.06605"
        }
    """

    print(json.loads(json.dumps(arxiv_doc, cls=srs.ArxivDocEncoder)))
    print(json.loads(expected_json))

    assert json.loads(json.dumps(arxiv_doc, cls=srs.ArxivDocEncoder)) == json.loads(expected_json)

def test_serialize_domain_arxivdocument_wrong_type():
    with pytest.raises(TypeError):
        json.dumps(datetime.datetime.now(), cls=srs.ArxivDocEncoder)
