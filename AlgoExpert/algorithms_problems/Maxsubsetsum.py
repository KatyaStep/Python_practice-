# def maxSubsetSumNoAdjacent(array):
#     # Write your code here.
#     max_sums = array[:]
#     max_sums[1] = max(array[0], array[1])
#
#     for i in range(2, len(array)):
#         max_sums[i] = max(max_sums[i-1],max_sums[i-2] + array[i])
#
#     return max_sums[-1]


def numberOfWaysToMakeChange(n, denoms):
    # Write your code here.
    if n == 0:
        return 1

    ways = [0] * (n + 1)
    ways[0] = 1

    for denom in denoms:
        for amount in range(1, len(ways)):
            if denom <= amount:
                ways[amount] += ways[amount - denom]

    return ways[n]


# my_array = [75, 105, 120, 75, 90, 135]
# # my_array = [1, 2, 3]
#
# print(maxSubsetSumNoAdjacent(my_array))

n = 7
denoms = [1, 5, 10, 25]

print(numberOfWaysToMakeChange(n, denoms))