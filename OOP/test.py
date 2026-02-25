# Create a class Cart with:

# attribute items — a list of tuples (name, price)
# __str__ → prints all items nicely
# __len__ → returns number of items
# __add__ → merges two carts into a new one
# __contains__ → checks if an item name is in the cart
# __getitem__ → lets you access items by index like cart[0]
# A property total → returns total price of all items


class Cart:

    # all_objects = []

    def __init__(self):
        self.items = []
        # self.name = name
        # Cart.all_objects.append(self)


    def __str__(self):
      return "\n".join(f"{item[0]}: ${item[1]}" for item in self.items)
    
    def __len__(self):
        return len(self.items)
    
    def __add__(self,other):

        new_cart = Cart()
        new_cart.items = self.items + other.items
        return new_cart


    def __contains__(self, name):
        return any(item[0] == name for item in self.items)
    
    def __getitem__(self,index):
        return self.items[index]
    
    @property
    def total(self):
        return sum(item[1] for item in self.items)
    


        





R = Cart()
R.items.append(("T-shirt",50))
R.items.append(("Pants",60))
R.items.append(('scarf',30))
R.items.append(('oppo',30))

print("T-shirt" in R)  # True
print("Shoes" in R)    # False

print(R[3])

R2 = Cart()
R2.items.append(("Bag",50))
R2.items.append(("hat",36))
R2.items.append(('dress',830))


o = (R + R2).items  
print(o) 

    



