import json
from flask import Blueprint, request, Response

from crawler.use_cases import request_objects as req
from crawler.shared import response_object as res
from crawler.repository import arxiv_repo as ar
from crawler.use_cases import arxiv_document_use_case as uc
from crawler.serializers.json import arxiv_document_serializer as ser

blueprint = Blueprint('arxiv', __name__)

STATUS_CODES = {
    res.ResponseSuccess.
    SUCCESS: 200,
    res.ResponseFailure.RESOURCE_ERROR: 404,
    res.ResponseFailure.PARAMETERS_ERROR: 400,
    res.ResponseFailure.SYSTEM_ERROR: 500
}

@blueprint.route('/arxiv', methods=['GET'])
def arxiv():
    qrystr_params = {
        'filters': {},
    }

    for arg, values in request.args.items():
        if arg.startswith('filter_'):
            qrystr_params['filters'][arg.replace('filter_', '')] = values

    request_object = req.ArxivDocumentListRequestObject.from_dict(qrystr_params)

    repo = ar.ArxivRepo()
    use_case = uc.ArxivDocumentListUseCase(repo)

    response = use_case.execute(request_object)

    return Response(json.dumps(response.value, cls=ser.ArxivDocEncoder),
                    mimetype='application/json',
                    status=STATUS_CODES[response.type])