"""Module doc string"""


def min_number_of_coins_change(change, denoms):
    """Returns the smallest number of coins needed to make change"""
    num_of_coins = [float("inf")] * (change + 1)
    num_of_coins[0] = 0

    for denom in denoms:
        for idx, amount in enumerate(num_of_coins):
            if denom <= idx:
                num_of_coins[idx] = min(amount, (1 + num_of_coins[idx - denom]))

    if num_of_coins[change] != float("inf"):
        return num_of_coins[change]

    return -1


# change = 7
# n = 135
# denoms = [39, 45, 130, 40, 4, 1, 60, 75]
coins = [1, 10, 5]
print(min_number_of_coins_change(7, coins))
