"""Takes the valid request object and returns a filtered arxiv document"""

import collections
from webminer.interface_adapters.rest_adapters import request_object as req


class ArxivDocumentListRequestObject(req.ValidRequestObject):
    """Creates an arxiv document list out of a request object

    Args:
        req (obj): Validated requested object

    Returns:
        class: For transforming the request into a dictionary
    """

    def __init__(self, filters=None):
        self.filters = filters

    @classmethod
    def from_dict(cls, adict):
        """Convert dictionary to Arxiv document object

        Args:
            adict (dict): a python dictionary

        Returns:
            dict: a filtered list object
        """

        invalid_req = req.InvalidRequestObject()

        if "filters" in adict and not isinstance(adict["filters"], collections.Mapping):
            invalid_req.add_error("filters", "Is not iterable")

        if invalid_req.has_errors():
            return invalid_req

        return ArxivDocumentListRequestObject(filters=adict.get("filters", None))
