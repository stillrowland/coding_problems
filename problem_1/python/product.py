from functools import reduce

def simple_product(array):
    product = reduce(lambda x, y: x * y, array)
    return list(map(lambda x: product / x, array))
