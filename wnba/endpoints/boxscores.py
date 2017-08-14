
from wnba.utils import clean_locals
from wnba.endpoints.baseendpoint import BaseEndpoint


class Boxscores(BaseEndpoint):

    def traditional(self, game_id, season):
        url = '%s%s/scores/gamedetail/%s_gamedetail.json' % (self.client.data_url, season, game_id)
        r = self.request(url, self.client.data_headers)
        return r

    def advanced(self, game_id, idx_data):
        """
        Get advanced box score stats for a given game.

        :param game_id: id for the game to get data for.
        :type game_id: str
        :param idx_data: the index to retrieve data from json.
        :type idx_data: int
        :returns: data for specified filters, as defined below by idx_data.
        :rtype: DataFrame

        ========   ============   ==================================================
        idx_data       Name                         Description
        ========   ============   ==================================================
            0       PlayerStats   Advanced box scores on an individual player basis.
            1       TeamStats     Advanced box scores on a team basis.
        ========   ============   ==================================================

        """
        params = clean_locals(locals())
        url = '%s%s' % (self.client.stats_url, 'wnbaadvancedboxscore')
        r = self.request(url, self.client.stats_headers, params=params)
        df = self.process_response(r, idx_data, 'resultSets')
        return df
