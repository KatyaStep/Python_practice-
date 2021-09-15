def sortedSquaredArray(array):
    array.sort()
    squared_array = []

    for value in array:
        squared_array.append(value * value)

    squared_array.sort()

    return squared_array


array = [-1, -2, 3, 5, 6, 8, 9]

print(sortedSquaredArray(array))