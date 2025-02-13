from __future__ import annotations
import os
from Libs.User import User

def getDirectories(path: str) -> list[str]:
    return os.walk(path)[1]

def Load():
    DATA_DIRECTORY: str = "Data"