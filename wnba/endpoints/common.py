
import pandas as pd

from wnba.endpoints.baseendpoint import BaseEndpoint


class Common(BaseEndpoint):

    def current_players(self, season):
        url = r'%s%s/players/10_player_info.json' % (self.client.data_url, season)
        r = self.request(url, self.client.data_headers)
        df = pd.DataFrame(r.get('pls', {}).get('pl', []))
        return df

    def historic_players(self, season):
        url = r'%s%s/players/10_historical_players.json' % (self.client.data_url, season)
        r = self.request(url, self.client.data_headers)
        df = pd.DataFrame(r.get('pls', {}).get('pl', []))
        return df

    def current_teams(self, season):
        url = r'%s%s/teams/10_team_info.json' % (self.client.data_url, season)
        r = self.request(url, self.client.data_headers)
        df = pd.DataFrame(r.get('tms', {}).get('t', []))
        return df
