from __future__ import annotations

import os

from SocialNetwork.Globals import Globals


# secure random string
def RandomStr(length: int) -> str:
    CHARS_LENGTH: int = len(Globals.VALID_CHARS)

    randomStr: str = ""
    randomBytes: bytes = os.urandom(length)

    for byte in randomBytes:
        i: int = 0
        iChar = 0

        while i != byte:
            i += 1
            iChar += 1
            if iChar == CHARS_LENGTH:
                iChar = 0
        randomStr += Globals.VALID_CHARS[iChar]
    return randomStr


if __name__ == "__main__":
    print(RandomStr(16))