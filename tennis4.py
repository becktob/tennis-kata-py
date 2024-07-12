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
            return format_score("Deuce", "")

        if self.serverHasWon():
            return format_score("Win for " + self.server, "")

        if self.receiverHasWon():
            return format_score("Win for " + self.receiver, "")

        if self.serverHasAdvantage():
            return format_score("Advantage " + self.server, "")

        if self.receiverHasAdvantage():
            return format_score("Advantage " + self.receiver, "")

        return format_score(self.scores[self.serverScore], self.scores[self.receiverScore])

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


def format_score(server_score: str, receiver_score: str) -> str:
    if "" == receiver_score:
        return server_score
    if server_score == receiver_score:
        return server_score + "-All"
    return server_score + "-" + receiver_score