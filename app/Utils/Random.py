from __future__ import annotations

import os


# secure random string
def RandomStr(length: int) -> str:
    CHARS: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    CHARS_LENGTH: int = len(CHARS)

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
        randomStr += CHARS[iChar]
    return randomStr


if __name__ == "__main__":
    print(RandomStr(16))