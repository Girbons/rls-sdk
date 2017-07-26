from requests import request

from .api_map import api_map
from .exceptions import (
    BadRequest,
    ResourceNotFound,
    Unauthorized,
    InternalServerError
)


class Api:
    def __init__(self):
        self.base_endpoint = api_map['current']['api_root']

    def request(self, url, method, api_key, **kwargs):
        complete_url = '{}{}'.format(self.base_endpoint, url)
        header = {'Authorization': api_key}
        response = request(method=method, url=complete_url, headers=header, **kwargs)
        return handle_response(response)


def handle_response(response):
    status_code = response.status_code
    if 200 <= status_code <= 299:
        return response
    elif status_code == 400:
        raise BadRequest
    elif status_code == 401:
        raise Unauthorized
    elif status_code == 404:
        raise ResourceNotFound
    elif status_code == 500:
        raise InternalServerError
