"""Create a class for applying use cases

Raises:
    NotImplementedError: If a use case cannot be implemented

Returns:
    class: UseCase class
"""

from webminer.shared import response_object as res


class UseCase(object):
    """Creates the UseCase class

    Args:
        object (obj): A base object

    Raises:
        NotImplementedError:
            If a a requested object cannot be implemented by the UseCase class

    Returns:
        class: Methods for executing and processing incoming requests
    """

    def execute(self, request_object):
        if not request_object:
            return res.ResponseFailure.build_from_invalid_request_object(request_object)
        try:
            return self.process_request(request_object)
        except Exception as exc:
            return res.ResponseFailure.build_system_error(
                f"{exc.__class__.__name__}: {exc}"
            )

    def process_request(self, request_object):
        raise NotImplementedError("process_request() not implemented by UseCase class")
