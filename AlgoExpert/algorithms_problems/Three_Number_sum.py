def threeNumberSUm(array, targetSum):
    # array.sort()
    # triplet = []
    # output = []
    # count = 0
    #
    # while count < len(array):
    #     for i in range(len(array)):
    #         sum_of_two = targetSum - array[i]
    #         for j in range(i+1, len(array)):
    #             third_num = sum_of_two - array[j]
    #             if third_num in array[j+1:]:
    #                 triplet.append([array[i], array[j], third_num])
    #         if len(triplet) != 0:
    #             output.extend(triplet)
    #         count += 1
    #         triplet = []
    # return output

    array.sort()
    triplets = []

    for i in range(len(array)):
        left = i+1
        right = len(array)-1

        while left < right:
            currentSum = array[i] + array[left] + array[right]
            if currentSum < targetSum:
                left += 1
            elif currentSum > targetSum:
                right -= 1
            else:
                triplets.append([array[i], array[left], array[right]])
                left += 1
                right -= 1
    return triplets

my_array = [12, 3, 1, 2, -6, 5, -8, 6]
targetSum = 0

print(threeNumberSUm(my_array, targetSum))