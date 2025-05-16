from __future__ import annotations

from SocialNetwork.Globals import Globals


class Hashtag:
    __Text: str

    def __init__(self, text: str):
        lowerText: str = text.lower()  # mette minuscolo
        textStr: list[str] = list(lowerText)
        formattedText: str = ""

        for i in range(0, len(textStr)):
            if textStr[i] not in Globals.VALID_CHARS:
                textStr[i] = "_" # if char not valid, change it to an underscore _

        for i in range(0, len(textStr)):
            formattedText += textStr[i]

        self.__Text = formattedText

    def __str__(self) -> str:
        return self.__Text

    @property
    def Text(self) -> str:
        return self.__Text

    def __eq__(self, other) -> bool:
        if isinstance(other, Hashtag):
            return self.Text == other.Text
        return False
