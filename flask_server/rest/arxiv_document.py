"""Defines the REST functionality and returns a response object"""

import logging

from flask import Blueprint, request, Response
import ujson

from webminer.use_cases.request_arxiv import arxiv_repo as ar
from webminer import process_arxiv_request as uc
from webminer.rest_adapters import request_objects as req
from webminer.shared import response_object as res
from webminer.serializers.json import arxiv_document_serializer as ser

STATUS_CODES = {
    res.ResponseSuccess.SUCCESS: 200,
    res.ResponseFailure.RESOURCE_ERROR: 404,
    res.ResponseFailure.PARAMETERS_ERROR: 400,
    res.ResponseFailure.SYSTEM_ERROR: 500,
}

LOGGER = logging.getLogger('flask.app')
sh = logging.StreamHandler()
sh.setLevel(logging.INFO)
LOGGER.addHandler(sh)

ARXIV = Blueprint("arxiv", __name__)



@ARXIV.route("/arxiv", methods=["GET"])
def arxiv():
    """
    Defines a GET route for the arxiv API.
    Make the request object API ready.
    Transform the response into JSON format

    Returns:
        object (JSON): A response object for further querying
    """

    qrystr_params = {"filters": {}}

    for arg, values in request.args.items():
        if arg.startswith("filter_"):
            qrystr_params["filters"][arg.replace("filter_", "")] = values

    request_object = req.ArxivDocumentListRequestObject.from_dict(qrystr_params)

    repo = ar.ArxivRepo()
    use_case = uc.ProcessArxivDocuments(repo)

    response = use_case.execute(request_object)

    return Response(
        ujson.dumps(response.value, cls=ser.ArxivDocEncoder),
        mimetype="application/json",
        status=STATUS_CODES[response.type],
    )
