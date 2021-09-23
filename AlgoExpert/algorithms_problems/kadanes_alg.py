from collections import defaultdict


def hasSingleCycle(array):
    # Write your code here.
    second_arr = defaultdict()
    idx = 0
    while idx < len(array):
        new_idx = calculate_new_idx(idx, array[idx], len(array))
        if new_idx not in second_arr:
            num = array[new_idx]
            second_arr[new_idx] = num
            idx = new_idx
        else:
            break

    print(second_arr)
    return len(array) == len(second_arr)


def calculate_new_idx(idx, num, length):
    next_idx = (idx + num) % length

    return next_idx


# print(hasSingleCycle([2, 3, 1, -4, -4, 2]))
# print(hasSingleCycle([2, 2, -1]))
# print(hasSingleCycle([1, 2, 3, 4, -2, 3, 7, 8, -26]))
# print(hasSingleCycle([1, -1, 1, -1]))
print(hasSingleCycle([10, 11, -6, -23, -2, 3, 88, 908, -26]))