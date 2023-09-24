from dataclasses import dataclass
from app.Classes.car import Car


@dataclass
class Customer:
    name: str
    product_cart: dict
    location: list
    money: int
    car: Car
