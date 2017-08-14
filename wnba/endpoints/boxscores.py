
from wnba.utils import clean_locals
from wnba.endpoints.baseendpoint import BaseEndpoint


class Boxscores(BaseEndpoint):

    def traditional(self, game_id, season):
        url = '%s%s/scores/gamedetail/%s_gamedetail.json' % (self.client.data_url, season, game_id)
        r = self.request(url, self.client.data_headers)
        return r

    def advanced(self, game_id):
        params = clean_locals(locals())
        url = '%s%s' % (self.client.stats_url, 'wnbaadvancedboxscore')
        r = self.request(url, self.client.stats_headers, params=params)
        return r
