def isMonotonic(array):
    monotonic_decrease = True
    monotonic_increase = True

    for i in range(1, len(array)):

        if array[i-1] > array[i]:
            monotonic_decrease = False
        elif array[i-1] < array[i]:
            monotonic_increase = False

    return monotonic_decrease or monotonic_increase




my_array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
# my_array = [-1, -5, -10, -1100, -900, -1101, -1102, -9001]

print(isMonotonic(my_array))
