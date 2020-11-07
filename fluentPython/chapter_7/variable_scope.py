# Function reading a local and a global variable.

from dis import dis

b = 6

def f1(a):
    print(a)
    print(b)

f1(3)

def f2(a):
    print(a)
    print(b)
    b = 9

# f2(3)   # UnboundLocalError: local variable 'b' referenced before assignment

def f3(a):
    global b
    print(a)
    print(b)
    b = 9

f3(3)
print(b)

print(dis(f1))
print(dis(f2))