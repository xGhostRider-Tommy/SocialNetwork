from __future__ import annotations

import bcrypt


# hash è un tipo di crittografia che serve per le password
def Hash(string: str) -> str:
    byteString: bytes = string.encode("utf-8") # trasforma in bytes

    salt: bytes = bcrypt.gensalt()
    hash: bytes = bcrypt.hashpw(byteString, salt)

    return hash.decode("utf-8") # da bytes a str

# per login
def CheckHash(unhashed: str, hashed: str) -> bool:
    firstHash: bytes = unhashed.encode("utf-8")
    secondHash: bytes = hashed.encode("utf-8")

    return bcrypt.checkpw(firstHash, secondHash)