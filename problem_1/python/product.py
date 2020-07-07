from functools import reduce
from operator import mul

def simple_product(array):
    product = reduce(mul, array)
    def divide_by_product(number):
        return product / number
    return list(map(divide_by_product, array))
