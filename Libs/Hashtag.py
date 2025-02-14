from __future__ import annotations

class Hashtag:
    __VALID_CHARS: str = "abcdefghijklmnopqrstuvwxyz1234567890"

    # do not use this
    def __init__(self):
        self.__Text: str = "hashtag" # placeholder

    # use this
    @staticmethod
    def getHashtag(text: str) -> Hashtag | None:
        lowerText = text.lower()
        hashtag: Hashtag

        for c in lowerText:
            if c not in Hashtag.__VALID_CHARS:
                return None

        hashtag = Hashtag()
        hashtag.__Text = lowerText
        return hashtag

    @property
    def Text(self):
        return self.__Text