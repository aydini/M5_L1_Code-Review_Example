import discount
from discount import Item

CART = [Item("pen", 10.0), Item("pad", 30.0)]
 
 
def show(label, fn, items, percent):
    try:
        print(f"{label:8} {percent:>5}% -> {fn(items, percent):.2f}")
    except Exception as e:
        print(f"{label:8} {percent:>5}% -> {type(e).__name__}: {e}")
 
 
def main():
    print("Cart with two items:")    
    for percent in (25, 0, 100, 150):
        show("discount", discount.apply_discount, CART, percent)
        print()

    print()
    print("empty cart:")
    show("discount", discount.apply_discount, [], 50)
 
 
if __name__ == "__main__":
    main()