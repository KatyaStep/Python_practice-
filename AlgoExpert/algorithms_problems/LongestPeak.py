def longestPeak(array):
    # isIncreased = True
    # isDecreased = False
    # peak = None
    # result = []
    # output = []

    # for i in range(1, len(array)):
    #     if isIncreased:
    #         if array[i] > array[i-1]:
    #             peak.append(array[i-1])
    #         elif array[i] < array[i-1]:
    #             if len(peak) != 0:
    #                 isIncreased = False
    #                 isDecreased = True
    #             else:
    #                 continue
    #         else:
    #             peak = []
    #             continue
    #
    #     if isDecreased:
    #         peak.append(array[i - 1])
    #         # if array[i] < array[i-1]:
    #         #     peak.append(array[i-1])
    #         if array[i] > array[i - 1]:
    #         # elif array[i] > array[i-1]:
    #         #     peak.append(array[i-1])
    #             isIncreased = True
    #             isDecreased = False
    #             peak = [peak[-1]]
    #         elif array[i] == array[i-1]:
    #             # peak.append(array[i])
    #             isIncreased = True
    #             isDecreased = False
    #             peak = []
    #         if i == len(array) -1:
    #             if array[i] < array[i - 1]:
    #                 peak.append(array[i])
    #
    #         if len(peak) > len(result):
    #             result = peak


    longest_peak = 0
    i = 1

    while i < len(array) - 1:
        if array[i-1] < array[i] and array[i+1] < array[i]:
            peak = array[i]
        else:
            i += 1
            continue

        left_idx = i - 2

        while left_idx >= 0 and array[left_idx] < array[left_idx + 1]:
            left_idx -= 1

        right_idx = i + 2

        while right_idx < len(array) and array[right_idx] < array[right_idx - 1]:
            right_idx += 1

        current_peak = right_idx - left_idx - 1
        longest_peak = max(current_peak, longest_peak)

        i = right_idx


    return longest_peak


# my_array = [1, 2, 3, 2, 1, 1]
# my_array = [1, 1, 1, 2, 3, 10, 12, -3, -3, 2, 3, 45, 800, 99, 98, 0, -1, -1, 2, 3, 4, 5, 0, -1, -1]

# my_array = [5, 4, 3, 2, 1, 2, 1]
# my_array = [1, 2, 3, 4, 5, 1]
my_array = [1, 3, 2]

# my_array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
print(longestPeak(my_array))
