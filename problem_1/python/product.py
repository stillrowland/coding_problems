from functools import reduce

def simple_product(array):
    product = reduce(lambda x, y: x * y, array)
    result = []
    for number in array:
        result.append(product / number)
    return result
