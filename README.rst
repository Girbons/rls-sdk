=======================
Rocket League Stats SDK
=======================

.. image:: https://travis-ci.org/Girbons/rls-sdk.svg?branch=devel
    :target: https://travis-ci.org/Girbons/rls-sdk

.. image:: https://coveralls.io/repos/github/Girbons/rls-sdk/badge.svg?branch=devel
    :target: https://coveralls.io/github/Girbons/rls-sdk?branch=devel

.. image:: https://readthedocs.org/projects/rocket-league-stats-sdk/badge/?version=devel
    :target: http://rocket-league-stats-sdk.readthedocs.io/en/latest/?badge=devel
    :alt: Documentation Status

.. image:: ./img/rls_partner_horizontal_large.png
    :alt: This app uses data provided by Rocket League Stats


Setup
=====

From the command line::

    pip install rls-sdk


Usage
=====

Get the API_KEY: https://developers.rocketleaguestats.com/

Check the documentation_.

.. _documentation: http://rocket-league-stats-sdk.readthedocs.io/en/devel/


Examples
========

.. code-block:: python

    from rls.rocket import RocketLeague

    rocket = RocketLeague(api_key=['Your API Key'])
    response = rocket.players.player(id='76561198079681869', platform=1)
    response.json()
    {'data': [
        {'avatar': 'http://cdn.akamai.steamstatic.com/steamcommunity/public/images/avatars/54/5452c0b1ef1c5fbe3db778665bf728574b916c2b_full.jpg',
       'createdAt': 1476863051,
       'displayName': 'Girbons',
       'lastRequested': 1501082634,
       'nextUpdateAt': 1501082812,
       'platform': {'id': 1, 'name': 'Steam'},
       'profileUrl': 'https://rocketleaguestats.com/profile/Steam/76561198079681869',
       'rankedSeasons': {'3': {'10': {'division': 0,
          'matchesPlayed': 7,
          'rankPoints': 409,
          'tier': 0},
         '11': {'division': 4, 'matchesPlayed': 657, 'rankPoints': 385, 'tier': 4},
         '12': {'division': 0, 'matchesPlayed': 5, 'rankPoints': 80, 'tier': 0},
         '13': {'division': 0, 'matchesPlayed': 2, 'rankPoints': 150, 'tier': 0}},
        '4': {'10': {'division': 2,
          'matchesPlayed': 10,
          'rankPoints': 507,
          'tier': 5},
         '11': {'division': 0, 'matchesPlayed': 394, 'rankPoints': 528, 'tier': 6},
         '12': {'division': 0, 'matchesPlayed': 3, 'rankPoints': 644, 'tier': 0},
         '13': {'division': 0, 'matchesPlayed': 5, 'rankPoints': 681, 'tier': 0}},
        '5': {'10': {'division': 0,
          'matchesPlayed': 17,
          'rankPoints': 600,
          'tier': 7},
         '11': {'division': 0, 'matchesPlayed': 610, 'rankPoints': 605, 'tier': 7},
         '12': {'division': 0, 'matchesPlayed': 3, 'rankPoints': 644, 'tier': 0},
         '13': {'division': 1,
          'matchesPlayed': 10,
          'rankPoints': 544,
          'tier': 6}}},
       'signatureUrl': 'http://signature.rocketleaguestats.com/normal/Steam/76561198079681869.png',
       'stats': {'assists': 1206,
        'goals': 2932,
        'mvps': 467,
        'saves': 1820,
        'shots': 5475,
        'wins': 1037},
       'uniqueId': '76561198079681869',
       'updatedAt': 1501082632}],
     'maxResultsPerPage': 20,
     'page': 0,
     'results': 1,
     'totalResults': 1
     }


Contribuiting
=============

Feel free to submit a Pull Request just follow the guidelines in the docs_.

.. _docs: http://rocket-league-stats-sdk.readthedocs.io/en/devel/contribuiting/
