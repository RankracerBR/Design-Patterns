from abc import ABC, abstractmethod


class Pizza(ABC):
    """ Classe Abstrata """
    def prepare(self) -> None:
        """ Template method """
        self.add_ingredients() # Abstract
        self.hook_before_add_ingredients() # Hook (estado ou ação do método)
        self.hook_after_add_ingredients() # 
        self.cook() # Abstract
        self.cut() # Concreto
        self.serve() # Concreto

    def hook_before_add_ingredients(self) -> None: pass
    def hook_after_add_ingredients(self) -> None: pass

    def cut(self) -> None:
        print(f'{self.__class__.__name__}: Cortando pizza.')
    
    def serve(self) -> None:
        print(f'{self.__class__.__name__}: Servindo pizza.')
    
    @abstractmethod
    def add_ingredients(self) -> None: pass

    @abstractmethod
    def cook(self) -> None: pass


class Amoda(Pizza):
    def add_ingredients(self) -> None:
        print(f'Amoda - adicionando ingredientes presunto, queijo, peperoni')

    def cook(self) -> None:
        print(f'Amoda - cozinhado por 45min no forno a lenha')


class Veg(Pizza):
    def hook_before_add_ingredients(self) -> None:
        print('Veg - Lavando ingredientes')

    def add_ingredients(self) -> None:
        print(f'Veg - adicionando ingredientes: ingredientes veganos')

    def cook(self) -> None:
        print(f'Veg - cozinhado por 5min no forno comum')
    

if __name__ == "__main__":
    a_moda = Amoda()
    a_moda.prepare()

    print()

    veg = Veg()
    veg.prepare()