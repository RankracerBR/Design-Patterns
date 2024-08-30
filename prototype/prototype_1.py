from __future__ import annotations
from typing import List


class StringReprMixin:
    def __str__(self):
        params = ', '.join([f'{k}={v}' for k, v in self.__dict__.items()])
        return f'{self.__class__.__name__}({params})'
    
    def __repr__(self): # Transforma objeto em string
        return self.__str__()


class Person(StringReprMixin):
    def __init__(self, firstname: str, lastname: str) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.addresses: List = []

    def add_address(self, address: Address) -> None:
        self.addresses.append(address)
    
    def clone(self) -> Person:
        return deepcopy(self)

class Address(StringReprMixin):
    def __init__(self, street, number) -> None:
        self.street = street
        self.number = number


if __name__ == "__main__":
    from copy import deepcopy

    augusto = Person('Augusto', 'Pontes')
    endereco_augusto = Address('Av. Brasil', '250A')
    augusto.add_address(endereco_augusto)

    esposa_augusto = augusto.clone()
    esposa_augusto.firstname = 'Júlia'
    print(augusto)
    print(esposa_augusto)