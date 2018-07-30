"""Create classes for different responses"""


class ResponseSuccess(object):
    """Creates a class for a successful response

    Args:
        object (obj): Base object to be extended

    Returns:
        boolean: True on success
    """

    SUCCESS = "SUCCESS"

    def __init__(self, value=None):
        self.type = self.SUCCESS
        self.value = value

    def __nonzero__(self):
        return True

    __bool__ = __nonzero__


class ResponseFailure(object):
    """Creates a class for a failed response

    Args:
        object (obj): Base object to be extended

    Returns:
        boolean: False on Failure
    """

    RESOURCE_ERROR = "RESOURCE_ERROR"
    PARAMETERS_ERROR = "PARAMETERS_ERROR"
    SYSTEM_ERROR = "SYSTEM_ERROR"

    def __init__(self, type_, message):
        self.type = type_
        self.message = self._format_message(message)

    def _format_message(self, msg):
        if isinstance(msg, Exception):
            return "{}: {}".format(msg.__class__.__name__, "{}".format(msg))
        return msg

    @property
    def value(self):
        return {"type": self.type, "message": self.message}

    def __bool__(self):
        return False

    @classmethod
    def build_resource_error(cls, message=None):
        return cls(cls.RESOURCE_ERROR, message)

    @classmethod
    def build_system_error(cls, message=None):
        return cls(cls.SYSTEM_ERROR, message)

    @classmethod
    def build_parameters_error(cls, message=None):
        return cls(cls.PARAMETERS_ERROR, message)

    @classmethod
    def build_from_invalid_request_object(cls, invalid_request_object):
        """Create an error message from an invalid requested object

        Args:
            invalid_request_object (obj): The requested object that is invalid

        Returns:
            string: The message consisting of the error parameters and the message
        """

        error_parameter = err["parameter"]
        error_message = err["message"]
        message = "\n".join(
            [
                f"{error_parameter}: {error_message}"
                for err in invalid_request_object.errors
            ]
        )
        return cls.build_parameters_error(message)
