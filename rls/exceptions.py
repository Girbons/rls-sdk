
class BadRequest(Exception):
    """
    400 Bad Request
    """


class ResourceNotFound(Exception):
    """
    404 Resource Not Found
    """


class Unauthorized(Exception):
    """
    401 Unauthorized
    """


class InternalServerError(Exception):
    """
    500 Internal Server Error
    """


class ConfigError(Exception):
    """
    Configuration not provided in api_map
    """


class MissingParam(Exception):
    """
    Wraps errors caught when setting up
    the url with its parameters
    """

    def __init__(self, param):
        """
        Initializes the exception with the
        missing parameter name
        `param`: The missing parameter
        """
        self.param = param

    def __str__(self):
        return 'Missing %s parameter' % self.param
