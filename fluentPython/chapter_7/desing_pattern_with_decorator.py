from abc import ABC, abstractmethod
from collections import namedtuple

from promotions import promos, best_promo

Customer = namedtuple('Customer', 'name fidelity')

class LineItem:
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity

class Order: # the context

    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion

    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion(self)
        return self.total() - discount

    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())


joe = Customer('Jhon Doe', 0)
ann = Customer('Ann Smith', 1100)

cart = [LineItem('banana', 4, .5),
        LineItem('apple', 10, 1.5),
        LineItem('watermellon', 5, 5.0)]
    
print(Order(joe, cart, best_promo))
print(Order(ann, cart, best_promo))

banana_cart = [LineItem('banana', 30, .5),
                LineItem('apple', 10, 1.5)]

print(Order(joe, banana_cart, best_promo))

long_order = [LineItem(str(item_code), 1, 1.0)
                for item_code in range(10)]

print(Order(joe, long_order, best_promo))
print(Order(joe, cart, best_promo))