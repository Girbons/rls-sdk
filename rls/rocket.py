from . import api_map

from .resolvers import Resolver
from .exceptions import ConfigError


default_api_map = api_map._API_MAP['current']['api']


class RocketLeague:
    def __init__(self, api_key, api_map=None, **kwargs):
        self.api_key = api_key
        if api_map:
            self.api_map = api_map
        else:
            self.api_map = default_api_map

    def __getattr__(self, name):
        if name not in self.api_map:
            raise ConfigError('COnfiguration not available in api_map for this call')
        instance = RocketLeague(self.api_key, api_map=self.api_map[name])
        setattr(self, name, instance)
        return instance

    def __call__(self, *args, **kwargs):
        resolver = Resolver()
        return resolver.resolve(self.api_key, api_map=self.api_map, **kwargs)
