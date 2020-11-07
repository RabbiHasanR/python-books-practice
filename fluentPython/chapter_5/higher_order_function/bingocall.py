# BingoCage does one thing: picks items from a shuffled
# list.
import random

class BingoCage:

    def __init__(self, items):
        self._items = list(items)
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')
    
    def __call__(self):
        return self.pick()


# Here is a simple demo of Example 5-8. Note how a bingo instance can be invoked as a
# function, and the callable(...) built-in recognizes it as a callable object.

bingo = BingoCage(range(10))
print(bingo.pick())
print(bingo())
print(callable(bingo))