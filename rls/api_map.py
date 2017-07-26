_API_MAP = {
    'current': {
        'api_root': 'https://api.rocketleaguestats.com/v1/',
        'api': {

            'data': {
                'platforms': {
                    'url': 'data/platforms',
                    'method': 'get'
                },

                'seasons': {
                    'url': 'data/seasons',
                    'method': 'get'
                },

                'playlists': {
                    'url': 'data/playlists',
                    'method': 'get'
                },

                'tiers': {
                    'url': 'data/tiers',
                    'method': 'get'
                },
            },

            'players': {
                'player': {
                    'url': 'player?unique_id={id}&platform_id={platform}',
                    'method': 'get'
                },

                'batch_players': {
                    'url': 'player/batch',
                    'method': 'post'
                },

                'search_players': {
                    'url': 'search/players?display_name={name}',
                    'method': 'get'
                },
            },

            'leaderboard': {
                'ranked': {
                    'url': 'leaderboard/ranked?playlist_id={id}',
                    'method': 'get'
                },

                'stat': {
                    'url': 'leaderboard/stat?type={type}',
                    'method': 'get'
                },
            }
        }
    }
}

api_map = _API_MAP
