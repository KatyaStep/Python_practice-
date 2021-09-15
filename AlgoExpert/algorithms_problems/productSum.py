import math
def product(array):
    result = []
    level_of_depth = 1

    __implmProductSum(level_of_depth, array, result)

    return sum(result)


def __implmProductSum(level_of_depth,  array, result):
    for element in array:
        if type(element) != int:
            __implmProductSum( level_of_depth + 1, element, result)
        else:
            result.append(math.factorial(level_of_depth) * element)

    level_of_depth -= 1
    return result


my_array = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
# my_array = [[[[[5]]]]]
print(product(my_array))
