"""Tests the arxiv repository
"""

import pytest

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


@pytest.fixture
def domain_arxivdocs():
    """Creates a fixture for the returned objects
    """
    return [arxiv_doc_1, arxiv_doc_2, arxiv_doc_3, arxiv_doc_4]


def assert_equal(arg1, arg2):
    if arg1 != arg2:
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
