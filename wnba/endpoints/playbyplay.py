
import requests
import pandas as pd

from wnba.endpoints.baseendpoint import BaseEndpoint


class PlayByPlay(BaseEndpoint):

    def play_by_play(self, game_id, season):
        def clean_data(raw_data):
            base_info = {k: v for k, v in raw_data.get('g').items() if k not in ['next', 'pla']}
            return [{**base_info, **event} for event in raw_data.get('g').get('pla')]
        data = []
        status_code = 200
        i = 1
        while status_code == 200:
            url = '%s%s/scores/pbp/%s_%s_pbp.json' % (self.client.data_url, season, game_id, i)
            r = requests.get(url, headers=self.client.data_headers)
            status_code = r.status_code
            if status_code == 200:
                data.extend(clean_data(r.json()))
            i += 1
        return pd.DataFrame(data)
