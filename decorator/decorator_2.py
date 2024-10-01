from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List
from copy import deepcopy


####### INGREDIENTS
@dataclass
class Ingredient:
    price: float


@dataclass
class Bread(Ingredient):
    price: float = 1.50


@dataclass
class Sausage(Ingredient):
    price: float = 4.99



@dataclass
class Bacon(Ingredient):
    price: float = 7.99



@dataclass
class Egg(Ingredient):
    price: float = 1.50


@dataclass
class Cheese(Ingredient):
    price: float = 6.35


@dataclass
class MashedPotatoes(Ingredient):
    price: float = 2.25


@dataclass
class PotatoeSticks(Ingredient):
    price: float = 0.99


# HotDogs
class HotDog:
    _name: str
    _ingredients: List[Ingredient]

    @property
    def price(self) -> float:
        return round(sum([
            ingredient.price for ingredient in self._ingredients
        ]), 2)

    @property
    def name(self) -> str: 
        return self._name
    
    @property
    def ingredients(self) -> List[Ingredient]:
        return self._ingredients

    def __repr__(self) -> str:
        return f'{self.name}({self.price}) -> {self.ingredients}'

class SimpleHotDog(HotDog):
    def __init__(self) -> None:
        self._name = 'SimpleHotDog'
        self._ingredients: List[Ingredient] = [
            Bread(),
            Sausage(),
            PotatoeSticks()
        ]

class SpecialHotDog(HotDog):
    def __init__(self) -> None:
        self._name = 'SpecialHotDog'
        self._ingredients: List[Ingredient] = [
            Bread(),
            Sausage(),
            Bacon(),
            Egg(),
            Cheese(),
            MashedPotatoes(),
            PotatoeSticks(),
        ]


# Decorators
class HotDogDecorator(HotDog):
    def __init__(self, hotdog: HotDog, ingredient: Ingredient) -> None:
        self.hotdog = hotdog
        self._ingredient = ingredient
        self._ingredients = deepcopy(self.hotdog.ingredients)
        self._ingredients.append(self._ingredient)

    @property
    def name(self) -> str: 
        return f'{self.hotdog.name} + {self._ingredient.__class__.__name__}'
    

if __name__ == "__main__":
    simple_hotdog = SimpleHotDog()
    print(simple_hotdog)

    bacon_simple_hotdog = HotDogDecorator(simple_hotdog, Bacon())
    egg_bacon_simple_hotdog = HotDogDecorator(bacon_simple_hotdog, Egg())

    mashed_potato_egg_bacon_simple_hotdog = HotDogDecorator(
        egg_bacon_simple_hotdog, 
        MashedPotatoes()
    )

    mashed_potato_egg_bacon_simple_hotdog = HotDogDecorator(
        egg_bacon_simple_hotdog, 
        MashedPotatoes()
    )

    print(mashed_potato_egg_bacon_simple_hotdog)