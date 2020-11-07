# Lists of factorials produced with map and filter compared to alterna‐
# tives coded as list comprehensionf
def factorial(n):
    """returns n!"""
    return 1 if n < 2 else n * factorial(n-1)

fact_list = list(map(factorial, range(6)))
print(fact_list)

fact_list_compreh = [factorial(i) for i in range(6)]
print(fact_list_compreh)

fact_filter_list = list(map(factorial, filter(lambda x: x % 2, range(6))))
print(fact_filter_list)

fact_filter_list_compreh = [factorial(i) for i in range(6) if i % 2]
print(fact_filter_list_compreh)