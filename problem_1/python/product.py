from functools import reduce
from operator import mul

def simple_product(array):
    product = reduce(mul, array)
    return list(map(lambda x: product / x, array))
