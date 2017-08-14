
import pandas as pd

from wnba.endpoints.baseendpoint import BaseEndpoint


class Scoreboard(BaseEndpoint):

    def scoreboard(self, month_no, season, result_only=True):
        if month_no < 10:
            month_no = '0%s' % month_no
        url = r'%s%s/league/10_league_schedule_%s.json' % (self.client.data_url, season, month_no)
        r = self.request(url, self.client.data_headers)
        game_info = [{
            **{k: v for k, v in game.items() if k not in ['bd', 'h', 'v', 'ptsls']},
            **{'h%s' % k: v for k, v in game.get('h', {}).items()},
            **{'a%s' % k: v for k, v in game.get('v', {}).items()},
        } for game in r.get('mscd', {}).get('g', [])]
        df = pd.DataFrame(game_info)
        if result_only:
            df = df[df.stt == 'Final']
        return df
