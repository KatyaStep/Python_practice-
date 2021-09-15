def binarySearch(array, target):
    # length_of_array = len(array)
    initial_array = array.copy()
    while len(array) >= 1:
        length_of_array = len(array)
        if target < array[length_of_array // 2]:
            array = array[:length_of_array // 2]
        elif target > array[length_of_array // 2]:
            array = array[length_of_array // 2:]
        else:
            if target in array:
                return initial_array.index(target)
            else:
                return -1
    # return False



my_array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
target = 0

print(binarySearch(my_array, target))