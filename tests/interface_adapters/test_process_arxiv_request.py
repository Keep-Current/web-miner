"""Testing the serialization of the use-case ouput
"""

from unittest import mock
import pytest

from webminer.entities.arxiv_document import ArxivDocument
from webminer.interface_adapters.rest_adapters import response_object as res
from webminer.interface_adapters.rest_adapters import request_objects as req
from webminer.interface_adapters import process_arxiv_request as uc


@pytest.fixture
def domain_arxivdocs():
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


def test_arxiv_doc_list_without_parameters(domain_arxivdocs):
    """Tests calling the ProcessArxivDocuments method without any params

    Args:
        domain_arxivdocs ([type]): the expected results

    Raises:
        AssertionError: If nothing was returned
        AssertionError: If the response is not the expected one
    """

    repo = mock.Mock()
    repo.list.return_value = domain_arxivdocs

    arxiv_doc_list_use_case = uc.ProcessArxivDocuments(repo)
    request_object = req.ArxivDocumentListRequestObject.from_dict({})

    response_object = arxiv_doc_list_use_case.execute(request_object)

    if not bool(response_object):
        raise AssertionError("response_object is empty")
    repo.list.assert_called_with(filters=None)

    if response_object.value != domain_arxivdocs:
        raise AssertionError("respons differs form expected")


def test_arxiv_doc_list_with_filters(domain_arxivdocs):
    """Tests calling the usecase filter with parameters
    TODO - implement that part.
    
    Args:
        domain_arxivdocs ([type]): The expected filtered documents
    """

    repo = mock.Mock()
    repo.list.return_value = domain_arxivdocs

    arxiv_doc_list_use_case = uc.ProcessArxivDocuments(repo)
    qry_filters = {"a": 5}
    request_object = req.ArxivDocumentListRequestObject.from_dict(
        {"filters": qry_filters}
    )

    response_object = arxiv_doc_list_use_case.execute(request_object)

    if not bool(response_object):
        raise AssertionError("response_object is empty")
    repo.list.assert_called_with(filters=qry_filters)
    if response_object.value != domain_arxivdocs:
        raise AssertionError("respons differs form expected")


def test_arxiv_doc_list_handles_generic_error():
    """Tests handling of a generic error when the request is empty
    """

    repo = mock.Mock()
    repo.list.side_effect = Exception("Just an error message")

    arxiv_doc_list_use_case = uc.ProcessArxivDocuments(repo)
    request_object = req.ArxivDocumentListRequestObject.from_dict({})

    response_object = arxiv_doc_list_use_case.execute(request_object)

    if bool(response_object):
        raise AssertionError("response_object supposed to be empty")
    if response_object.value != {
        "type": res.ResponseFailure.SYSTEM_ERROR,
        "message": "Exception: Just an error message",
    }:
        raise AssertionError("error response differs from expected")


def test_arxiv_doc_list_handles_bad_request():
    """Tests handling a usecase with a bad request
    """

    repo = mock.Mock()

    arxiv_doc_list_use_case = uc.ProcessArxivDocuments(repo)
    request_object = req.ArxivDocumentListRequestObject.from_dict({"filters": 5})

    response_object = arxiv_doc_list_use_case.execute(request_object)

    if bool(response_object):       
        raise AssertionError("response_object supposed to be empty")
    if response_object.value != {
        "type": res.ResponseFailure.PARAMETERS_ERROR,
        "message": "filters: Is not iterable",
    }:
        raise AssertionError("error response differs from expected")
