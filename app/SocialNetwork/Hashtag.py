from __future__ import annotations

class Hashtag:
    __VALID_CHARS: str = "abcdefghijklmnopqrstuvwxyz1234567890"

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
            if c not in Hashtag.__VALID_CHARS:
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