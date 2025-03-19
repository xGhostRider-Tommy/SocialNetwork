from __future__ import annotations


class Image:
    __Extension: str
    __Bytes: bytes

    def __init__(self, extension: str, photo: bytes):
        self.__Extension = extension
        self.__Bytes = photo

    @property
    def Extension(self) -> str:
        return self.__Extension

    @property
    def Content(self) -> bytes:
        return self.__Bytes