from typing import Literal

class Item():
    name: str
    category: Literal["alcohol", "tobacco", "food"]

    def __init__(self, name: str, category: Literal["alcohol", "tobacco", "food"]):
        self.name = name
        self.category = category


def _can_purchase_tobacco_us(age: int) -> bool:
    return age >= 21

def _can_purchase_tobacco_eu(age: int) -> bool:
    return age >= 18

def _can_purchase_alcohol_us(age: int) -> bool:
    return age >= 21

def _can_purchase_alcohol_eu(age: int) -> bool:
    return age >= 16

def can_purchase(item: Item, purchaser_age: int, location: Literal["us", "eu"]) -> bool:
    if item.category == 'alcohol':
        if location == 'eu':
            return _can_purchase_alcohol_eu(purchaser_age)
        else:
            return _can_purchase_alcohol_us(purchaser_age)
    elif item.category == 'tobacco':
        if location == 'eu':
            return _can_purchase_tobacco_eu(purchaser_age)
        else:
            return _can_purchase_tobacco_us(purchaser_age)
    else:
        return True