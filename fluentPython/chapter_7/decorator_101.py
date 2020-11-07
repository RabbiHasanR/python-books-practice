# A decorator usually replaces a function with a different one.

def deco(func):
    def inner():
        print('running inner()')
    return inner

@deco
def target():
    print('running target()')

target()