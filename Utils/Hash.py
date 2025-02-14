from __future__ import annotations

import bcrypt


def Hash(string: str) -> str:
    byteString: bytes = string.encode("utf-8")

    salt: bytes = bcrypt.gensalt()
    hash: bytes = bcrypt.hashpw(byteString, salt)

    return hash.decode("utf-8")

def CheckHash(first: str, second: str) -> bool:
    firstHash: bytes = first.encode("utf-8")
    secondHash: bytes = second.encode("utf-8")

    return bcrypt.checkpw(firstHash, secondHash)