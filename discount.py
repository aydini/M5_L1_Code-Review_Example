"""The code after review. Each change answers one review comment."""
 
from dataclasses import dataclass
 
 
@dataclass
class Item:
    name: str
    price: float
 
 
def apply_discount(items, percent):
    """Return the total price of items, reduced by percent.
 
    percent must be between 0 and 100. An empty list returns 0.0.
    Does not modify items.
    """
    if not 0 <= percent <= 100:
        raise ValueError(f"percent must be between 0 and 100, got {percent}")
    subtotal = sum(item.price for item in items)
    return subtotal * (1 - percent / 100)