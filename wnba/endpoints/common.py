
from wnba.endpoints.baseendpoint import BaseEndpoint


class Common(BaseEndpoint):

    def current_players(self, season):
        url = r'%s%s/players/10_player_info.json' % (self.client.data_url, season)
        r = self.request(url, self.client.data_headers)
        return r

    def historic_players(self, season):
        url = r'%s%s/players/10_historical_players.json' % (self.client.data_url, season)
        r = self.request(url, self.client.data_headers)
        return r

    def current_teams(self, season):
        url = r'%s%s/teams/10_team_info.json' % (self.client.data_url, season)
        r = self.request(url, self.client.data_headers)
        return r
