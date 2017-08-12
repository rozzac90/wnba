
from wnba.baseclient import BaseClient
from wnba import endpoints


class APIClient(BaseClient):

    def __init__(self):
        super(APIClient, self).__init__()

        self.boxscores = endpoints.Boxscores(self)
        self.common = endpoints.Common(self)
        self.playbyplay = endpoints.PlayByPlay(self)
        self.player = endpoints.Player(self)
        self.scoreboard = endpoints.Scoreboard(self)
        self.team = endpoints.Team(self)
