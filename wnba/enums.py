class _DefaultN:
    Default = 'N'


class _DefaultBlank:
    Default = ''


class _DefaultZero:
    Default = '0'


class LeagueID:
    NBA = '00'
    Default = NBA


class Weight(_DefaultBlank):
    All = ''
    Over200 = 'GT 200'
    Under200 = 'LT 200'
    Over225 = 'GT 225'
    Under225 = 'LT 225'
    Over250 = 'GT 250'
    Under250 = 'LT 250'
    Over275 = 'GT 275'
    Under275 = 'LT 275'
    Over300 = 'GT 300'
    Under300 = 'LT 300'


class Season:
    Current = '2016-17'
    Default = Current


class PtMeasureType:
    CatchAndShoot = 'CatchShoot'
    Defense = 'Defense'
    Drives = 'Drives'
    Passing = 'Passing'
    TouchesAndPossessions = 'Possessions'
    PullUpShooting = 'PullUpShot'
    Rebounding = 'Rebounding'
    ShootingEfficiency = 'Efficiency'
    SpeedAndDistance = 'SpeedDistance'
    ElbowTouch = 'ElbowTouch'
    PostTouch = 'PostTouch'
    PaintTouch = 'PaintTouch'


class PORound(_DefaultBlank):
    All = ''
    ConferenceQuarters = '1'
    ConferenceSemis = '2'
    ConferenceFinals = '3'
    Finals = '4'


class Height(_DefaultBlank):
    All = ''
    Over6 = 'GT 6-0'
    Under6 = 'LT 6-0'
    Over63 = 'GT 6-3'
    Under63 = 'LT 6-3'
    Over67 = 'GT 6-7'
    Under67 = 'LT 6-7'
    Over610 = 'GT 6-10'
    Under610 = 'LT 6-10'
    Over7 = 'GT 7-0'
    Under7 = 'LT 7-0'


class Country(_DefaultBlank):
    pass


class PlayerExperience(_DefaultBlank):
    All = ''
    Rookie = 'Rookie'
    Sophomore = 'Sophomore'
    Veteran = 'Veteran'


class PlayerPosition(_DefaultBlank):
    All = ''
    Centre = 'C'
    Guard = 'G'
    Forward = 'F'


class College(_DefaultBlank):
    pass


class Conference(_DefaultBlank):
    All = ''
    East = 'East'
    West = 'West'


class DraftPick(_DefaultBlank):
    pass


class DraftYear(_DefaultBlank):
    pass


class Division(_DefaultBlank):
    All = ''
    Atlantic = 'Atlantic'
    Central = 'Central'
    Northwest = 'Northwest'
    Pacific = 'Pacific'
    Southeast = 'Southeast'
    Southwest = 'Southwest'


class ClutchTime:
    All = ''
    mins5 = 'Last 5 Minutes'
    mins4 = 'Last 4 Minutes'
    mins3 = 'Last 3 Minutes'
    mins2 = 'Last 2 Minutes'
    mins1 = 'Last 1 Minutes'
    secs30 = 'Last 30 Seconds'
    secs10 = 'Last 10 Seconds'
    Default = All


class AheadBehind:
    All = 'Ahead or Behind'
    BehindOrTied = 'Behind or Tied'
    AheadOrTied = 'Ahead or Tied'
    Default = All


class PerMode:
    Totals = 'Totals'
    PerGame = 'PerGame'
    MinutesPer = 'MinutesPer'
    Per48 = 'Per48'
    Per40 = 'Per40'
    Per36 = 'Per36'
    PerMinute = 'PerMinute'
    PerPossession = 'PerPossession'
    PerPlay = 'PerPlay'
    Per100Possessions = 'Per100Possessions'
    Per100Plays = 'Per100Plays'
    Default = Totals


class SeasonType:
    Regular = 'Regular Season'
    Playoffs = 'Playoffs'
    PreSeason = 'Pre Season'
    AllStars = 'All Star'
    Default = Regular


class MeasureType:
    Traditional = 'Base'
    Advanced = 'Advanced'
    Misc = 'Misc'
    FourFactors = 'Four Factors'
    Scoring = 'Scoring'
    Opponent = 'Opponent'
    Usage = 'Usage'
    Default = Traditional


class GroupQuantity:
    Default = 5


class Outcome(_DefaultBlank):
    Win = 'W'
    Loss = 'L'


class Location(_DefaultBlank):
    Home = 'Home'
    Away = 'Away'


class SeasonSegment(_DefaultBlank):
    EntireSeason = ''
    PreAllStar = 'Pre All-Star'
    PostAllStar = 'Post All-Star'


class DateFrom(_DefaultBlank):
    pass


class DateTo(_DefaultBlank):
    pass


class VsConference(_DefaultBlank):
    All = ''
    East = 'East'
    West = 'West'


class VsDivision(_DefaultBlank):
    All = ''
    Atlantic = 'Atlantic'
    Central = 'Central'
    Northwest = 'Northwest'
    Pacific = 'Pacific'
    Southeast = 'Southeast'
    Southwest = 'Southwest'


class GameSegment(_DefaultBlank):
    EntireGame = ''
    FirstHalf = 'First Half'
    SecondHalf = 'Second Half'
    Overtime = 'Overtime'


class ShotClockRange(_DefaultBlank):
    AllRanges = ''
    ShotClockOff = 'ShotClock Off'
    Immediate = '24-22'
    VeryEarly = '22-18 Very Early'
    Early = '18-15 Early'
    Average = '15-7 Average'
    Late = '7-4 Late'
    VeryLate = '4-0 Very Late'


class DribbleRange:
    All = ''
    NoDribble = '0 Dribbles'
    Dribble1 = '1 Dribble'
    Dribble2 = '2 Dribbles'
    Between3and6Dribbles = '3-6 Dribbles'
    Over7Dribbles = '7+ Dribbles'


class CloseDefDistRange:
    All = ''
    VeryTight = '0-2 Feet - Very Tight'
    Tight = '2-4 Feet - Tight'
    Open = '4-6 Feet - Open'
    WideOpen = '6+ Feet - Wide Open'
    Between2And4 = '2-4 Feet - Tight'
    Default = All


class GeneralRange:
    All = ''
    Overall = 'Overall'
    CatchAndShoot = 'Catch and Shoot'
    PullUp = 'Pull Up'
    Under10Ft = 'Less than 10 ft'
    Default = All


class PlusMinus(_DefaultN):
    pass


class PaceAdjust(_DefaultN):
    pass


class Rank(_DefaultN):
    pass


class OpponentTeamID(_DefaultZero):
    pass


class Period(_DefaultBlank):
    AllQuarters = '0'
    FirstQuarter = '1'
    SecondQuarter = '2'
    ThirdQuarter = '3'
    FourthQuarter = '4'

    def Overtime(self, n):
        return str(4 + n)


class LastNGames(_DefaultZero):
    pass


class PlayOffRound(_DefaultZero):
    All = '0'
    QuarterFinals = '1'
    SemiFinals = '2'
    ConferenceFinals = '3'
    Finals = '4'


class Month(_DefaultZero):
    All = '0'
    October = '1'
    November = '2'
    December = '3'
    January = '4'
    February = '5'
    March = '6'
    April = '7'
    May = '8'
    June = '9'
    July = '10'
    August = '11'
    September = '12'


class RangeType(_DefaultZero):
    pass


class StartRange(_DefaultZero):
    pass


class EndRange(_DefaultZero):
    pass


class StartPeriod(Period):
    pass


class EndPeriod(Period):
    pass


class Stat:
    PTS = 'PTS'
    FGM = 'FGM'
    FGA = 'FGA'
    FG_PCT = 'FG%'
    FG3M = '3PM'
    FG3A = '3PA'
    FG3_PCT = '3P%'
    FTM = 'FTM'
    FTA = 'FTA'
    FT_PCT = 'FT%'
    OREB = 'OREB'
    DREB = 'DREB'
    REB = 'REB'
    AST = 'AST'
    STL = 'STL'
    BLK = 'BLK'
    TOV = 'TOV'
    EFF = 'EFF'
    AST_TOV = 'AST/TO'
    STL_TOV = 'STL/TOV'
    PF = 'PF'
    Default = PTS


class StatType:
    Traditional = 'Traditional'
    Advanced = 'Advanced'
    Tracking = 'Tracking'
    Default = Traditional


class StatCategory:
    Points = 'Points'
    Rebounds = 'Rebounds'
    Assists = 'Assists'
    Defense = 'Defense'
    Clutch = 'Clutch'
    Playmaking = 'Playmaking'
    Efficiency = 'Efficiency'
    FastBreak = 'Fast Break'
    Scoring = 'ScoringBreakdown'
    Default = Points


class Scope:
    AllPlayers = 'S'
    Rookies = 'Rookies'
    Default = AllPlayers


class PlayerScope:
    AllPlayers = 'All Players'
    Rookies = 'Rookie'
    Default = AllPlayers


class PlayerOrTeam:
    Player = 'Player'
    Team = 'Team'
    Default = Player


class GameScope:
    Blank = ''
    Season = 'Season'
    Last10 = 'Last 10'
    Yesterday = 'Yesterday'
    Finals = 'Finals'
    Default = Season


class DistanceRange:
    Blank = ''
    Zone = 'By Zone'
    Ft5 = '5ft Range'
    Ft8 = '8ft Range'
    Default = Zone


class Counter:
    Default = 0


class Direction:
    Descending = 'DESC'
    Ascending = 'ASC'
    Default = Descending


class DefenseCategory:
    Overall = 'Overall'
    Point2 = '2 Pointers'
    Point3 = '3 Pointers'
    Under6Ft = 'Less Than 6Ft'
    Under10Ft = 'Less Than 10Ft'
    Over15Ft = 'Greater Than 15Ft'
    Default = Overall


class StarterBench:
    All = ''
    Starter = 'Starters'
    Bench = 'Bench'
    Default = All


class TeamID:
    All = '0'
    Default = All


class ContextMeasure:
    FGM = 'FGM'
    FGA = 'FGA'
    FG_PCT = 'FG_PCT'
    FG3M = 'FG3M'
    FG3A = 'FG3A'
    FG3_PCT = 'FG3_PCT'
    PF ='PF'
    EFG_PCT = 'EFG_PCT'
    TS_PCT = 'TS_PCT'
    PTS_FB = 'PTS_FB'
    PTS_OFF_TOV = 'PTS_OFF_TOV'
    PTS_2ND_CHANCE = 'PTS_2ND_CHANCE'
    Default = FGA


class Default_Values:
    Blank = ''
    Zero = 0
