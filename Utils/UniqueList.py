from __future__ import annotations

from typing import TypeVar, Generic, Iterator

T: type = TypeVar("T")

class UniqueList(Generic[T]):
    __List: list[T]

    def __init__(self, list: list[T]):
        self.__List = []
        
        for element in list:
            if element not in self.__List:
                self.__List.append(element)

    # True if success, False if error
    def Add(self, element: T) -> bool:
        condition: bool = element not in self.__List
        
        if condition:
            self.__List.append(element)
        return condition
    
    def Remove(self, index: int) -> None:
        self.__List.pop(index)

    def __len__(self) -> int:  # per far funzionare len(oggetto)
        return len(self.__List)

    def __getitem__(self, index: int) -> T:
        return self.__List[index]

    def __iter__(self) -> Iterator[T]:
        return iter(self.__List)

    def __str__(self) -> str:
        string: str = ""

        for element in self.__List:
            string += str(element) + " "
        string = string[:-1]  # leva l'ultimo spazio
        string += ""

        return string