import pytest

from rls.rocket import RocketLeague
from rls.exceptions import MissingParam, ConfigError

from .utils import API_KEY


def test_rocket():
    rocket = RocketLeague(API_KEY)
    response = rocket.players.player(id='76561198079681869', platform=1)
    assert response.status_code == 200


def test_rocket_missing_params():
    rocket = RocketLeague(API_KEY)
    with pytest.raises(MissingParam) as exc:
        rocket.players.player(id='76561198079681869')
    assert str(exc.value) == "Missing 'platform' parameter"


def test_rocket_missing_api():
    rocket = RocketLeague(API_KEY)
    with pytest.raises(ConfigError) as exc:
        rocket.fake.fake()
    assert str(exc.value) == "Configuration not available in api_map for this call"
