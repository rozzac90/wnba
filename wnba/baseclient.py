
import requests


class BaseClient(object):
    def __init__(self):
        self.stats_url = 'http://stats.nba.com/stats/'
        self.data_url = 'http://data.wnba.com/data/5s/v2015/json/mobile_teams/wnba/'
        self.session = requests.Session()
        self.current_season = '2017'

    @property
    def stats_headers(self):
        """Set headers to be used in API requests."""
        return {'Content-Type': 'application/json',
                'user-agent': ('Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                               'AppleWebKit/537.36 (KHTML, like Gecko)'
                               'Chrome/60.0.3112.90 Safari/537.36'),
                'referer': 'http://www.wnba.com/stats/',
                'host': 'stats.nba.com',
                "cache-control": "max-age=0",
                'connection': 'keep-alive',
                "accept-encoding": "Accepflate, sdch",
                'accept-language': 'he-IL,he;q=0.8,en-US;q=0.6,en;q=0.4'}

    @property
    def data_headers(self):
        return {'Content-Type': 'application/json',
                'user-agent': ('Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                               'AppleWebKit/537.36 (KHTML, like Gecko)'
                               'Chrome/60.0.3112.90 Safari/537.36'),
                'referer': 'http://www.wnba.com/players/',
                'host': 'data.wnba.com',
                "cache-control": "max-age=0",
                'connection': 'keep-alive',
                "accept-encoding": "Accepflate, sdch",
                'accept-language': 'he-IL,he;q=0.8,en-US;q=0.6,en;q=0.4'}
