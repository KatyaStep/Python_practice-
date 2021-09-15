def mergeOverlappingIntervals(intervals):
    # intervals.sort()
    # overlapping_intervals = []
    # first_num = 0
    # second_num = 1
    # current_interval = intervals[0]
    #
    # for i in range(1, len(intervals)):
    #     if intervals[i][first_num] > current_interval[second_num]:
    #         overlapping_intervals.append(current_interval)
    #     else:
    #          intervals[i][first_num] = intervals[i-1][first_num]
    #          intervals[i][second_num] = max(intervals[i-1][second_num], intervals[i][second_num])
    #
    #     current_interval = intervals[i]
    #
    # overlapping_intervals.append(current_interval)
    #
    # return overlapping_intervals

    #Algo Expert solution
    sortedIntervals = sorted(intervals, key=lambda x: x[0])
    mergedIntervals = []
    currentInterval = sortedIntervals[0]
    mergedIntervals.append(currentInterval)

    for nextInterval in sortedIntervals:
        _, currentIntervalEnd = currentInterval
        nextIntervalStart, nextIntervalEnd = nextInterval

        if currentIntervalEnd >= nextIntervalStart:
            currentInterval[1] = max(currentIntervalEnd, nextIntervalEnd)
        else:
            currentInterval = nextInterval
            mergedIntervals.append(currentInterval)

    return mergedIntervals


my_intervals = [[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]]
# my_intervals = [[100, 105], [1, 104]]
print(mergeOverlappingIntervals(my_intervals))
