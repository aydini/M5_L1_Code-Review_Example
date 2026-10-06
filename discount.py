"""The code under review has five issues:
1. It does not validate that percent is between 0 and 100.
2. The function parameters and return value have no type annotations.
3. The index-based loop requires a sized, indexable collection.
4. The subtotal is accumulated manually instead of using sum().
5. Float arithmetic can introduce rounding errors for monetary values.
"""
 
from dataclasses import dataclass
 
 
@dataclass
class Item:
    name: str
    price: float
 
 
def apply_discount(items, percent):
    """Apply a percentage discount to all items."""
    total = 0
    for i in range(len(items)):
        total += items[i].price
    return total - (total * percent / 100)
