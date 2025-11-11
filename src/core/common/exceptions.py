class ApiException(Exception):
    """API Exception"""

    def __init__(self, message: str, status_code: int = 500):
        self.status_code = status_code
        self.message = message
        super().__init__(message)


class BadRequestApiException(ApiException):
    """The server could not understand the request due to invalid syntax."""

    def __init__(self, message: str):
        super().__init__(message, status_code=400)


class DuplicateEntryException(BadRequestApiException):
    """The server is does not allow multiple entries with the same name."""

    def __init__(self, message: str):
        super().__init__(message)


class UnauthorizedApiException(ApiException):
    """Although the HTTP standard specifies "unauthorized", semantically this response means
    "unauthenticated". That is, the client must validate_credentials itself to get the requested
     response.
    """

    def __init__(self, message: str):
        super().__init__(message, status_code=401)


class UnauthorizedServiceAccountException(UnauthorizedApiException):
    """Although the HTTP standard specifies "unauthorized", semantically this response means
    "unauthenticated". Some of the API require a privileged account in order to perform an
    operation.  Although a 401 status code, this exception allows a client to distinguish
    between a regular client authentication failure and privileged failure.
    """

    def __init__(self, message: str):
        super().__init__(message)


class ForbiddenApiException(ApiException):
    """The client does not have access rights to the content; that is, it is unauthorized, so the
    server is refusing to give the requested resource. Unlike 401, the client's identity is known
    to the server.
    """

    def __init__(self, message: str):
        super().__init__(message, status_code=403)


class ExpiredTokenException(ApiException):
    """Raise expired token condition. E.g. OAuth Token"""

    def __init__(self, message: str):
        super().__init__(message, status_code=403)


class PasswordPolicyException(ForbiddenApiException):
    """The client fails to modify a known users password because the Password fails the servers
    password policy. E.g. the password repeats, or is too simple. Unlike 401, the client's identity
    is known to the server.
    """

    def __init__(self, message: str):
        super().__init__(message)


class PasswordExpiredException(ForbiddenApiException):
    """The client successfully authenticates the user credentials, yet the users password is expired
    and user must change it. Unlike 401, the client's identity is known to the server.
    """

    def __init__(self, message: str):
        super().__init__(message)


class NotFoundApiException(ApiException):
    """The server can not find requested resource. In the browser, this means the URL is not
    recognized. In an API, this can also mean that the endpoint is valid but the resource itself
    does not exist. Servers may also send this response instead of 403 to hide the existence of a
    resource from an unauthorized client. This response code is probably the most famous one due to
    its frequent occurrence on the web.
    """

    def __init__(self, message: str):
        super().__init__(message, status_code=404)


class MethodNotAllowedApiException(ApiException):
    """The request method is known by the server but has been disabled and cannot be used. For
    example, an API may forbid DELETE-ing a resource. The two mandatory methods, GET and HEAD, must
    never be disabled and should not return this error code.
    """

    def __init__(self, message: str):
        super().__init__(message, status_code=405)


class ConflictApiException(ApiException):
    """This response is sent when a request conflicts with the current state of the server."""

    def __init__(self, message: str):
        super().__init__(message, status_code=409)


class TooManyRequestsApiException(ApiException):
    """The user has sent too many requests in a given amount of time ("rate limiting")."""

    def __init__(self, message: str):
        super().__init__(message, status_code=429)


class InternalErrorApiException(ApiException):
    """The server has encountered a situation it doesn't know how to handle."""

    def __init__(self, message: str):
        super().__init__(message, status_code=500)


class NotImplementedApiException(ApiException):
    """The request method is not supported by the server and cannot be handled. The only methods
    that servers are required to support (and therefore that must not return this code) are GET and
    HEAD.
    """

    def __init__(self, message: str):
        super().__init__(message, status_code=501)


class BadGatewayApiException(ApiException):
    """This error response means that the server, while working as a gateway to get a response
    needed to handle the request, got an invalid response.
    """

    def __init__(self, message: str):
        super().__init__(message, status_code=502)


class ServiceUnavailable(ApiException):
    """The server is not ready to handle the request. Common causes are a server that is down for
    maintenance or that is overloaded. Note that together with this response, a user-friendly page
    explaining the problem should be sent. This responses should be used for temporary conditions
    and the Retry-After: HTTP header should, if possible, contain the estimated time before the
    recovery of the service. The webmaster must also take care about the caching-related headers
    that are sent along with this response, as these temporary condition responses should usually
    not be cached.
    """

    def __init__(self, message: str):
        super().__init__(message, status_code=503)


ERROR_CODE_TO_EXCEPTION = {
    400: BadRequestApiException,
    401: UnauthorizedApiException,
    403: ForbiddenApiException,
    404: NotFoundApiException,
    405: MethodNotAllowedApiException,
    409: ConflictApiException,
    429: TooManyRequestsApiException,
    500: InternalErrorApiException,
    501: NotImplementedApiException,
    502: BadGatewayApiException,
    503: ServiceUnavailable,
}
