class Product:

    def __init__(self, name, price, discount):

        if len(name) == 0:
            raise ValueError("Name cannot be empty")
        self._name = name

        if price <= 0:
            raise ValueError("Price must be greater than zero")
        self._price = price

        if discount < 0 or discount > 100:
            raise ValueError("Discount must be between 0 and 100")
        self._discount = discount

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @property
    def discount(self):
        return self._discount

    @property
    def final_price(self):
        return self.price * (1 - self.discount / 100)


pro2 = Product("Book", 100, 10)
print(pro2.name)
print(pro2.final_price)   

#=================================================
import math

class Circle:

    def __init__(self, r):
        self._radius = None
        self.radius = r  


    @property
    def radius(self):
        return self._radius
    

    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Radius must be greater than 0")
        self._radius = value


    @radius.deleter
    def radius(self):
        print("Radius deleted")
        del self._radius


    @property
    def diameter(self):
        return self._radius * 2
    
    
    @property
    def area(self):
        return math.pi * self._radius ** 2



  


c = Circle(5)
print(c.area())
     
        





