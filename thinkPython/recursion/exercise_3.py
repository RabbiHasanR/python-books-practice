def is_power(a, b):
    """Return true if a divisible by b"""
    try:
        if a % b == 0:
            return True
    except ZeroDivisionError:
        raise ValueError('Invaid input')
    else:
        return False

try:
    print(is_power(5, 0))
except ValueError:
    print('Invalid input')