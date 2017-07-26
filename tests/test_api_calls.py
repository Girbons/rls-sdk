from rls.rocket import RocketLeague

from .utils import API_KEY


def test_platform_calls():
    rocket = RocketLeague(API_KEY)

    response = rocket.data.platforms()
    assert response.status_code == 200

    response = rocket.data.seasons()
    assert response.status_code == 200

    response = rocket.data.playlists()
    assert response.status_code == 200

    response = rocket.data.tiers()
    assert response.status_code == 200


def test_players_calls():
    rocket = RocketLeague(API_KEY)

    response = rocket.players.player(id='76561198079681869', platform=1)
    assert response.status_code == 200

    players = [
        {"platformId": "1", "uniqueId": "76561198033338223"},
        {"platformId": "1", "uniqueId": "76561197981122126"},
        {"platformId": "3", "uniqueId": "Loubleezy"},
        {"platformId": "2", "uniqueId": "Wizwonk"}
    ]
    response = rocket.players.batch_players(json=players)
    assert response.status_code == 200

    response = rocket.players.search_players(name="Girbons")
    assert response.status_code == 200


def test_leaderboard_calls():
    rocket = RocketLeague(API_KEY)

    response = rocket.leaderboard.ranked(id=10)
    assert response.status_code == 200

    response = rocket.leaderboard.stat(type="win")
    assert response.status_code == 200
