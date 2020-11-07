# Listing attributes of functions that don’t exist in plain instances.

class C: pass
obj = C()
print(dir(obj))

def func(): pass
print(dir(func))

differenc = sorted(set(dir(func)) - set(dir(obj)))
print(differenc)