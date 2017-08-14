
from wnba.endpoints.baseendpoint import BaseEndpoint


class Scoreboard(BaseEndpoint):

    def scoreboard(self, month_no, season):
        if month_no < 10:
            month_no = '0%s' % month_no
        url = r'%s%s/league/10_league_schedule_%s.json' % (self.client.data_url, season, month_no)
        r = self.request(url, self.client.data_headers)
        return r
