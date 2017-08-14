
import pandas as pd

from wnba import enums
from wnba.utils import clean_locals
from wnba.endpoints.baseendpoint import BaseEndpoint


class Team(BaseEndpoint):

    def team_roster(self, season, team_abbrev):
        def clean_data(raw_data):
            base_info = {k: v for k, v in raw_data.get('t', {}).items() if k not in ['pl']}
            return [{**base_info, **event} for event in raw_data.get('t').get('pl')]
        url = r'%s%s/teams/%s_roster.json' % (self.client.data_url, season, team_abbrev)
        r = self.request(url, self.client.data_headers)
        df = pd.DataFrame(clean_data(r))
        return df

    def all_advanced_stats(self, last_n_days=enums.LastNGames.Default, last_n_games=enums.LastNGames.Default,
                           league_id=enums.LeagueID.Default, location=enums.Location.Default, month=enums.Month.Default,
                           outcome=enums.Outcome.Default, per_mode=enums.PerMode.Totals, season=enums.Season.Default,
                           season_segment=enums.SeasonSegment.Default, season_type=enums.SeasonType.Default,
                           vs_team_id=''):
        """
        Team advanced stats breakdown.

        :param league_id: ID of the league to get data for. Default 00. Required.
        :type league_id: nba.enums.LeagueID
        :param season: Season to get players from. Required.
        :type season: nba.enums.Season
        :param season_type: part of season to pull data from. Required.
        :type season_type: nba.enums.SeasonType
        :param per_mode: grouping of stat data. Totals or PerGame accepted. Required.
        :type per_mode: nba.enums.PerMode
        :param outcome: Filter to only include stats for won or lost games. Default '' returns all. Required.
        :type outcome: nba.enums.Outcome
        :param location: Filter for home or road games only. Default '' returns all. Required.
        :type location: nba.enums.Location
        :param month: Filter for games occurring in a specific month (relative to season start). Default 0 returns all. Required.
        :type month: nba.enums.Month
        :param season_segment: Filter to only include stats from Post/Pre all star break. Default '' returns all. Required
        :type season_segment: nba.enums.SeasonSegment
        :param last_n_days: Filter stats for only those occurring in the last n days. Default '' includes all games. Required.
        :type last_n_days: nba.enums.LastNGames
        :param last_n_games: Filter stats for only those occurring in the last n games. Default '' includes entire games. Required.
        :type last_n_games: nba.enums.LastNGames
        :param vs_team_id:
        :type vs_team_id: int
        :returns: Team stats after applying all filters.
        :rtype: DataFrame

        """
        params = clean_locals(locals())
        url = '%s%s' % (self.client.stats_url, 'wnbaseasonsortableteamadvanced')
        r = self.request(url, self.client.stats_headers, params=params)
        df = self.process_response(r, 0, 'resultSets')
        return df

    def all_raw_stats(self, last_n_days=enums.LastNGames.Default, last_n_games=enums.LastNGames.Default,
                      league_id=enums.LeagueID.Default, location=enums.Location.Default, month=enums.Month.Default,
                      outcome=enums.Outcome.Default, per_mode=enums.PerMode.Totals, season=enums.Season.Default,
                      season_segment=enums.SeasonSegment.Default, season_type=enums.SeasonType.Default, vs_team_id=''):
        """
        Team stats breakdown.

        :param league_id: ID of the league to get data for. Default 00. Required.
        :type league_id: nba.enums.LeagueID
        :param season: Season to get players from. Required.
        :type season: nba.enums.Season
        :param season_type: part of season to pull data from. Required.
        :type season_type: nba.enums.SeasonType
        :param per_mode: grouping of stat data. Totals or PerGame accepted. Required.
        :type per_mode: nba.enums.PerMode
        :param outcome: Filter to only include stats for won or lost games. Default '' returns all. Required.
        :type outcome: nba.enums.Outcome
        :param location: Filter for home or road games only. Default '' returns all. Required.
        :type location: nba.enums.Location
        :param month: Filter for games occurring in a specific month (relative to season start). Default 0 returns all. Required.
        :type month: nba.enums.Month
        :param season_segment: Filter to only include stats from Post/Pre all star break. Default '' returns all. Required
        :type season_segment: nba.enums.SeasonSegment
        :param last_n_days: Filter stats for only those occurring in the last n days. Default '' includes all games. Required.
        :type last_n_days: nba.enums.LastNGames
        :param last_n_games: Filter stats for only those occurring in the last n games. Default '' includes entire games. Required.
        :type last_n_games: nba.enums.LastNGames
        :param vs_team_id:
        :type vs_team_id: int
        :returns: Team stats after applying all filters.
        :rtype: DataFrame

        """
        params = clean_locals(locals())
        url = '%s%s' % (self.client.stats_url, 'wnbaseasonsortableteamstats')
        r = self.request(url, self.client.stats_headers, params=params)
        df = self.process_response(r, 0, 'resultSets')
        return df
