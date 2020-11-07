import time

# from simple_decorator_example import clocks
from improve_clock_decorator import clocks

@clocks
def snooze(seconds):
    time.sleep(seconds)

@clocks
def factorial(n):
    return 1 if n < 2 else n * factorial(n-1)

if __name__=='__main__':
    print('*' * 40, 'Calling snooze(.123)')
    snooze(.123)
    print('*' * 40, 'Calling factorial(6)')
    print('6! =', factorial(6))