from __future__ import annotations
from typing import List, Dict


class Client:
    """Context"""
    
    def __init__(self, name) -> None:
        self.name = name
        self._addresses: List = []
        
        # Extrinsic address data
        self._address_number: str
        self._address_details: str
        
    def add_address(self, address: Address) -> None:
        self._addresses.append(address)
    
    def list_addresses(self) -> None:
        for address in self._addresses:
            address.show_address(self._address_number, self._address_details)
        

class Address:
    """Flyweight"""
    def __init__(self, street: str, neighbourhood: str, zip_code: str) -> None:
        self._street = street
        self._neighbourhood = neighbourhood
        self._zip_code = zip_code
    
    def show_address(self, address_number: str, address_details: str) -> None:
        print(
            self._street, address_number, self._neighbourhood, address_details,
            self._zip_code
        )
    
class AddressFactory:
    _addresses: Dict = {}
    
    def _get_key(self, **kwargs) -> str:
        return ''.join(kwargs.values())
    
    def get_address(self, **kwargs) -> Address:
        key = self._get_key(**kwargs)
        
        try:
            address_flyweight = self._addresses[key]
            print('Usando objeto já criado')
        except KeyError:
            address_flyweight = Address(**kwargs)
            self._addresses[key] = address_flyweight
            print('Criando novo objeto')
            
        return address_flyweight

if __name__ == "__main__":
    address_factory = AddressFactory()
    
    a1 = address_factory.get_address(street='Av Brasil',
                                     neighbourhood='Centro',
                                     zip_code='00000-0000'
                                    )
    
    a2 = address_factory.get_address(street='Av Brasil',
                                     neighbourhood='Centro',
                                     zip_code='00000-0000'
                                    )
    
    augusto = Client('Augusto')
    augusto._address_number = '50'
    augusto._address_details = 'Casa'
    augusto.add_address(a1)
    augusto.list_addresses()
    
    joana = Client('Joana')
    joana._address_number = '250A'
    joana._address_details = 'AP 555'
    joana.add_address(a2)
    joana.list_addresses()
    
    print(a1 == a2)
    
    