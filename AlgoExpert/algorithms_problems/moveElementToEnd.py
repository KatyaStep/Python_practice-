def moveElementToEnd(array, toMove):
    array.sort()
    # idx = []
    # for i in range(len(array)):
    #     if array[i] == toMove:
    #         idx.append(i)
    # for j in range(len(idx)):
    #     array.append(toMove)
    #     array.pop(idx[0])

    left = 0
    right = len(array) - 1

    while array[left] != array[right]:
        if array[left] == toMove:
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1
        else:
            left += 1

    return array

my_array = [2, 1, 2, 2, 2, 3, 4, 2]
toMove = 2

print(moveElementToEnd(my_array, toMove))