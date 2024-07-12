# -*- coding: utf-8 -*-

# TODO: rename to TennisGame if API allows for that
class TennisGame4:
    def __init__(self, server: str, receiver: str):
        self.server = server
        self.receiver = receiver
        self.serverScore = 0
        self.receiverScore = 0
        self.scores = ["Love", "Fifteen", "Thirty", "Forty"]

    # TODO: playerName -> player_name
    def won_point(self, playerName: str) -> None:
        if self.server == playerName:
            self.serverScore += 1
        else:
            self.receiverScore += 1

    def score(self) -> str:
        if self.isDeuce():
            return TennisResult("Deuce", "").format()

        if self.serverHasWon():
            return TennisResult("Win for " + self.server, "").format()

        if self.receiverHasWon():
            return TennisResult("Win for " + self.receiver, "").format()

        if self.serverHasAdvantage():
            return TennisResult("Advantage " + self.server, "").format()

        if self.receiverHasAdvantage():
            return TennisResult("Advantage " + self.receiver, "").format()

        return TennisResult(self.scores[self.serverScore], self.scores[self.receiverScore]).format()

    def receiverHasAdvantage(self) -> bool:
        return self.receiverScore >= 4 and (self.receiverScore - self.serverScore) == 1

    def serverHasAdvantage(self) -> bool:
        return self.serverScore >= 4 and (self.serverScore - self.receiverScore) == 1

    def receiverHasWon(self) -> bool:
        return self.receiverScore >= 4 and (self.receiverScore - self.serverScore) >= 2

    def serverHasWon(self) -> bool:
        return self.serverScore >= 4 and (self.serverScore - self.receiverScore) >= 2

    def isDeuce(self) -> bool:
        return self.serverScore >= 3 and self.receiverScore >= 3 and (self.serverScore == self.receiverScore)


class TennisResult:
    def __init__(self, serverScore: str, receiverScore: str):
        self.serverScore = serverScore
        self.receiverScore = receiverScore

    def format(self) -> str:
        if "" == self.receiverScore:
            return self.serverScore
        if self.serverScore == self.receiverScore:
            return self.serverScore + "-All"
        return self.serverScore + "-" + self.receiverScore
