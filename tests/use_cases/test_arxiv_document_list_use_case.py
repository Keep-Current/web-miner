import pytest
from unittest import mock

from webminer.entities.arxiv_document import ArxivDocument
from webminer.interface_adapters import response_object as res
from webminer.interface_adapters import request_objects as req
from webminer.interface_adapters import arxiv_document_use_case as uc


@pytest.fixture
def domain_storagerooms():
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

    return [arxiv_doc_1, arxiv_doc_2, arxiv_doc_3, arxiv_doc_4]


def test_arxiv_doc_list_without_parameters(domain_storagerooms):
    repo = mock.Mock()
    repo.list.return_value = domain_storagerooms

    arxiv_doc_list_use_case = uc.ArxivDocumentListUseCase(repo)
    request_object = req.ArxivDocumentListRequestObject.from_dict({})

    response_object = arxiv_doc_list_use_case.execute(request_object)

    assert bool(response_object) is True
    repo.list.assert_called_with(filters=None)

    assert response_object.value == domain_storagerooms


def test_arxiv_doc_list_with_filters(domain_storagerooms):
    repo = mock.Mock()
    repo.list.return_value = domain_storagerooms

    arxiv_doc_list_use_case = uc.ArxivDocumentListUseCase(repo)
    qry_filters = {"a": 5}
    request_object = req.ArxivDocumentListRequestObject.from_dict(
        {"filters": qry_filters}
    )

    response_object = arxiv_doc_list_use_case.execute(request_object)

    assert bool(response_object) is True
    repo.list.assert_called_with(filters=qry_filters)
    assert response_object.value == domain_storagerooms


def test_arxiv_doc_list_handles_generic_error():
    repo = mock.Mock()
    repo.list.side_effect = Exception("Just an error message")

    arxiv_doc_list_use_case = uc.ArxivDocumentListUseCase(repo)
    request_object = req.ArxivDocumentListRequestObject.from_dict({})

    response_object = arxiv_doc_list_use_case.execute(request_object)

    assert bool(response_object) is False
    assert response_object.value == {
        "type": res.ResponseFailure.SYSTEM_ERROR,
        "message": "Exception: Just an error message",
    }


def test_arxiv_doc_list_handles_bad_request():
    repo = mock.Mock()

    arxiv_doc_list_use_case = uc.ArxivDocumentListUseCase(repo)
    request_object = req.ArxivDocumentListRequestObject.from_dict({"filters": 5})

    response_object = arxiv_doc_list_use_case.execute(request_object)

    assert bool(response_object) is False
    assert response_object.value == {
        "type": res.ResponseFailure.PARAMETERS_ERROR,
        "message": "filters: Is not iterable",
    }
