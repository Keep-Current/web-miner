"""Defines the REST functionality and returns a response object"""

import json
from flask import Blueprint, request, Response

from webminer.use_cases.request_arxiv import arxiv_repo as ar
from webminer.interface_adapters import process_arxiv_request as uc
from webminer.interface_adapters.rest_adapters import request_objects as req
from webminer.interface_adapters.rest_adapters import response_object as res
from webminer.interface_adapters.serializers.json import arxiv_document_serializer as ser

blueprint = Blueprint("arxiv", __name__)

STATUS_CODES = {
    res.ResponseSuccess.SUCCESS: 200,
    res.ResponseFailure.RESOURCE_ERROR: 404,
    res.ResponseFailure.PARAMETERS_ERROR: 400,
    res.ResponseFailure.SYSTEM_ERROR: 500,
}


@blueprint.route("/arxiv", methods=["GET"])
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
        json.dumps(response.value, cls=ser.ArxivDocEncoder),
        mimetype="application/json",
        status=STATUS_CODES[response.type],
    )
