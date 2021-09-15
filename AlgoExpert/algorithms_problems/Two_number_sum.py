#"""O(n^2) complexity solution"""
#def twoNumberSum(array, targetSum):
#     N = len(array)
#
#     for i in range(N-1):
#         first_num = array[i]
#         if array[i + 1:] is not None:
#             for j in array[i+1:]:
#                 second_num = j
#                 if first_num + second_num == targetSum:
#                     return [first_num, second_num]
#     return []


# array = [3, 5, -4, 8, 11, 1, -1, 6]
# targetSum = 10
#
# print(twoNumberSum(array, targetSum))


# """O(n) complexity solution"""
#
# def twoNumberSum(array, targetSum):
#     nums = {}
#     for num in array:
#         potentialMatch = targetSum - num
#         if potentialMatch in nums:
#             return [num, potentialMatch]
#         else:
#             nums[num] = True
#     return []
#
#
# array = [3, 5, -4, 8, 11, 1, -1, 6]
# targetSum = 10
#
# print(twoNumberSum(array, targetSum))

"""O(nlog(n)) complexity solution"""

def twoNumberSum(array, targetSum):
    array.sort()
    leftPointer = 0
    rightPointer = len(array) - 1

    while leftPointer < rightPointer:
        current_sum = array[leftPointer] + array[rightPointer]
        if current_sum == targetSum:
            return [array[leftPointer], array[rightPointer]]
        elif current_sum < targetSum:
            leftPointer += 1
        else:
            rightPointer -= 1
    return []


array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10

print(twoNumberSum(array, targetSum))
