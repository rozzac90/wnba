
from wnba import enums
from wnba.utils import clean_locals
from wnba.endpoints.baseendpoint import BaseEndpoint


class Player(BaseEndpoint):

    def all_advanced_stats(self, last_n_days=enums.LastNGames.Default, last_n_games=enums.LastNGames.Default,
                           league_id=enums.LeagueID.Default, location=enums.Location.Default, month=enums.Month.Default,
                           outcome=enums.Outcome.Default, per_mode=enums.PerMode.Totals, season=enums.Season.Default,
                           season_segment=enums.SeasonSegment.Default, season_type=enums.SeasonType.Default,
                           vs_team_id='', player_experience=enums.PlayerExperience.Default, days_rest='',
                           conference=enums.Conference.Default, starter_bench=enums.StarterBench.Default,
                           player_position=enums.PlayerPosition.Default):
        """
        Team advanced stats breakdown.

        :param league_id: ID of the league to get data for. Default 00. Required.
        :type league_id: wnba.enums.LeagueID
        :param season: Season to get players from. Required.
        :type season: wnba.enums.Season
        :param season_type: part of season to pull data from. Required.
        :type season_type: wnba.enums.SeasonType
        :param per_mode: grouping of stat data. Totals or PerGame accepted. Required.
        :type per_mode: wnba.enums.PerMode
        :param outcome: Filter to only include stats for won or lost games. Default '' returns all. Required.
        :type outcome: wnba.enums.Outcome
        :param location: Filter for home or road games only. Default '' returns all. Required.
        :type location: wnba.enums.Location
        :param month: Filter for games occurring in a specific month (relative to season start). Default 0 returns all. Required.
        :type month: wnba.enums.Month
        :param season_segment: Filter to only include stats from Post/Pre all star break. Default '' returns all. Required
        :type season_segment: wnba.enums.SeasonSegment
        :param last_n_days: Filter stats for only those occurring in the last n days. Default '' includes all games. Required.
        :type last_n_days: wnba.enums.LastNGames
        :param last_n_games: Filter stats for only those occurring in the last n games. Default '' includes entire games. Required.
        :type last_n_games: wnba.enums.LastNGames
        :param vs_team_id: filter for stats vs a specific team.
        :type vs_team_id: int
        :param days_rest: minimum number of days rest prior to game for stats to be included.
        :type days_rest: int
        :param player_experience: Filter to only include players of specific experience level. Default '' returns all.
        :type player_experience: wnba.enums.PlayerExperience
        :param player_position: Filter to only include players of certain position. Default '' returns all.
        :type player_position: wnba.enums.PlayerPosition
        :param starter_bench: Filter to only include starts or bench. Default '' returns all.
        :type starter_bench: wnba.enums.StarterBench
        :param conference: Filter for teams from specific conference. Default '' returns all.
        :type conference: wnba.enums.Conference
        :returns: Team stats after applying all filters.
        :rtype: DataFrame

        """
        params = clean_locals(locals())
        url = '%s%s' % (self.client.stats_url, 'wnbaseasonsortableplayeradvanced')
        r = self.request(url, self.client.stats_headers, params=params)
        df = self.process_response(r, 0, 'resultSets')
        return df

    def all_raw_stats(self, last_n_days=enums.LastNGames.Default, last_n_games=enums.LastNGames.Default,
                      league_id=enums.LeagueID.Default, location=enums.Location.Default, month=enums.Month.Default,
                      outcome=enums.Outcome.Default, per_mode=enums.PerMode.Totals, season=enums.Season.Default,
                      season_segment=enums.SeasonSegment.Default, season_type=enums.SeasonType.Default,
                      vs_team_id='', player_experience=enums.PlayerExperience.Default, days_rest='',
                      conference=enums.Conference.Default, starter_bench=enums.StarterBench.Default,
                      player_position=enums.PlayerPosition.Default):
        """
        Player stats breakdown.

        :param league_id: ID of the league to get data for. Default 00. Required.
        :type league_id: wnba.enums.LeagueID
        :param season: Season to get players from. Required.
        :type season: wnba.enums.Season
        :param season_type: part of season to pull data from. Required.
        :type season_type: wnba.enums.SeasonType
        :param per_mode: grouping of stat data. Totals or PerGame accepted. Required.
        :type per_mode: wnba.enums.PerMode
        :param outcome: Filter to only include stats for won or lost games. Default '' returns all. Required.
        :type outcome: wnba.enums.Outcome
        :param location: Filter for home or road games only. Default '' returns all. Required.
        :type location: wnba.enums.Location
        :param month: Filter for games occurring in a specific month (relative to season start). Default 0 returns all. Required.
        :type month: wnba.enums.Month
        :param season_segment: Filter to only include stats from Post/Pre all star break. Default '' returns all. Required
        :type season_segment: wnba.enums.SeasonSegment
        :param last_n_days: Filter stats for only those occurring in the last n days. Default '' includes all games. Required.
        :type last_n_days: wnba.enums.LastNGames
        :param last_n_games: Filter stats for only those occurring in the last n games. Default '' includes entire games. Required.
        :type last_n_games: wnba.enums.LastNGames
        :param vs_team_id: filter for stats vs a specific team.
        :type vs_team_id: int
        :param days_rest: minimum number of days rest prior to game for stats to be included.
        :type days_rest: int
        :param player_experience: Filter to only include players of specific experience level. Default '' returns all.
        :type player_experience: wnba.enums.PlayerExperience
        :param player_position: Filter to only include players of certain position. Default '' returns all.
        :type player_position: wnba.enums.PlayerPosition
        :param starter_bench: Filter to only include starts or bench. Default '' returns all.
        :type starter_bench: wnba.enums.StarterBench
        :param conference: Filter for teams from specific conference. Default '' returns all.
        :type conference: wnba.enums.Conference
        :returns: Team stats after applying all filters.
        :rtype: DataFrame

        """
        params = clean_locals(locals())
        url = '%s%s' % (self.client.stats_url, 'wnbaseasonsortableplayerstats')
        r = self.request(url, self.client.stats_headers, params=params)
        df = self.process_response(r, 0, 'resultSets')
        return df

    def all_season_stats(self, last_n_days=enums.LastNGames.Default, last_n_games=enums.LastNGames.Default,
                         league_id=enums.LeagueID.Default, location=enums.Location.Default, month=enums.Month.Default,
                         outcome=enums.Outcome.Default, per_mode=enums.PerMode.Totals, season=enums.Season.Default,
                         season_segment=enums.SeasonSegment.Default, season_type=enums.SeasonType.Default,
                         vs_team_id='', player_experience=enums.PlayerExperience.Default, days_rest='',
                         conference=enums.Conference.Default, starter_bench=enums.StarterBench.Default,
                         player_position=enums.PlayerPosition.Default, top_x='',
                         stat_category=enums.Stat.Default):
        """
        Player stats breakdown.

        :param league_id: ID of the league to get data for. Default 00. Required.
        :type league_id: wnba.enums.LeagueID
        :param season: Season to get players from. Required.
        :type season: wnba.enums.Season
        :param season_type: part of season to pull data from. Required.
        :type season_type: wnba.enums.SeasonType
        :param per_mode: grouping of stat data. Totals or PerGame accepted. Required.
        :type per_mode: wnba.enums.PerMode
        :param outcome: Filter to only include stats for won or lost games. Default '' returns all. Required.
        :type outcome: wnba.enums.Outcome
        :param location: Filter for home or road games only. Default '' returns all. Required.
        :type location: wnba.enums.Location
        :param month: Filter for games occurring in a specific month (relative to season start). Default 0 returns all. Required.
        :type month: wnba.enums.Month
        :param season_segment: Filter to only include stats from Post/Pre all star break. Default '' returns all. Required
        :type season_segment: wnba.enums.SeasonSegment
        :param last_n_days: Filter stats for only those occurring in the last n days. Default '' includes all games. Required.
        :type last_n_days: wnba.enums.LastNGames
        :param last_n_games: Filter stats for only those occurring in the last n games. Default '' includes entire games. Required.
        :type last_n_games: wnba.enums.LastNGames
        :param vs_team_id: filter for stats vs a specific team.
        :type vs_team_id: int
        :param days_rest: minimum number of days rest prior to game for stats to be included.
        :type days_rest: int
        :param player_experience: Filter to only include players of specific experience level. Default '' returns all.
        :type player_experience: wnba.enums.PlayerExperience
        :param player_position: Filter to only include players of certain position. Default '' returns all.
        :type player_position: wnba.enums.PlayerPosition
        :param starter_bench: Filter to only include starts or bench. Default '' returns all.
        :type starter_bench: wnba.enums.StarterBench
        :param conference: Filter for teams from specific conference. Default '' returns all.
        :type conference: wnba.enums.Conference
        :param top_x: only return top x players.
        :type top_x: int
        :param stat_category: stat by which to sort players.
        :type stat_category: wnba.enums.Stat
        :returns: Team stats after applying all filters.
        :rtype: DataFrame

        """
        params = clean_locals(locals())
        url = '%s%s' % (self.client.stats_url, 'wnbaseasonstats')
        r = self.request(url, self.client.stats_headers, params=params)
        df = self.process_response(r, 0, 'resultSets')
        return df
