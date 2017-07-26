from .api import Api
from .exceptions import MissingParam


class Resolver:
    def __init__(self):
        self.url = ''
        self.method = ''
        self.api = Api()

    def setup(self, api_map=None, **kwargs):
        url = api_map['url']
        method = api_map['method']

        try:
            url = url.format(**kwargs)
        except KeyError as param:
            raise MissingParam(param)

        self.method = method
        self.url = url

    def resolve(self, api_key, api_map=None, **kwargs):
        self.setup(api_map=api_map, **kwargs)
        return self.api.request(url=self.url, method=self.method, api_key=api_key)
