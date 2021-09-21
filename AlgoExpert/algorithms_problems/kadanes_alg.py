def kadanes_algorithm(array):
    max_so_far = array[0]
    max_end_here = array[0]

    for idx in range(1, len(array)):
        num = array[idx]
        max_end_here = max(num, max_end_here+num)
        max_so_far = max(max_end_here, max_so_far)

    return max_so_far

print(kadanes_algorithm([3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]))
# print(kadanes_algorithm([-10]))