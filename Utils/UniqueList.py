from __future__ import annotations

from typing import TypeVar, Generic, Iterator

T = TypeVar("T")

class UniqueList(Generic[T]):
    def __init__(self, list: list[T]):
        self.__List: list[T] = []
        
        for element in list:
            if element not in self.__List:
                self.__List.append(element)
    
    def __len__(self) -> int: # per far funzionare len(oggetto)
        return len(self.__List)
    
    def __getitem__(self, index: int) -> T:
        return self.__List[index]
    
    def __iter__(self) -> Iterator[T]:
        return iter(self.__List)
    
    def Add(self, element: T) -> bool:
        condition: bool = element not in self.__List
        
        if condition:
            self.__List.append(element)
        return condition
    
    def Remove(self, index: int):
        self.__List.remove(index)