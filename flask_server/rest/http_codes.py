"""Returns Server Codes and info for HTTP requests"""
from webminer.shared import response_object as res

STATUS_CODES = {
    res.ResponseSuccess.SUCCESS: 200,
    res.ResponseFailure.RESOURCE_ERROR: 404,
    res.ResponseFailure.PARAMETERS_ERROR: 400,
    res.ResponseFailure.SYSTEM_ERROR: 500,
}

def http_codes():
    """Return dictionary of status codes

    SUCCESS: 200,
    RESOURCE_ERROR: 404,
    PARAMETERS_ERROR: 400,
    SYSTEM_ERROR: 500,
    """
    return STATUS_CODES