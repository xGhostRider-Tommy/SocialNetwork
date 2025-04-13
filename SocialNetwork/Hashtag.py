from __future__ import annotations

from SocialNetwork.Globals import Globals


class Hashtag:
    __Text: str

    # do not use this
    def __init__(self):
        pass

    # use this
    @staticmethod
    def getHashtag(text: str) -> Hashtag | None:
        lowerText = text.lower() # mette minuscolo
        hashtag: Hashtag

        for c in lowerText:
            if c not in Globals.VALID_CHARS:
                return None

        hashtag = Hashtag()
        hashtag.__Text = lowerText
        return hashtag

    def __str__(self) -> str:
        return self.__Text

    @property
    def Text(self):
        return self.__Text

    def __eq__(self, other):
        if isinstance(other, Hashtag):
            return self.Text == other.Text
        return False