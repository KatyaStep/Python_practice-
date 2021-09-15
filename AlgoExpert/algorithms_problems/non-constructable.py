from itertools import combinations

def nonConstructibleChange(coins):
    coins.sort()
    N = len(coins)

    all_possible_sum = set()

    for i in range(1, N+1):
        comb = combinations(coins, i)
        for j in list(comb):
            all_possible_sum.add((sum(j)))

    isEmpty = len(all_possible_sum)
    print(all_possible_sum)
    # max_num_in_seq = list(all_possible_sum)[-1]+2
    # seq_of_numbers = list(range(1, max_num_in_seq))

    # print(seq_of_numbers)

    if isEmpty != 0:
        max_num_in_seq = list(all_possible_sum)[-1] + 1
        seq_of_numbers = list(range(1, max_num_in_seq + 1))
        for num in seq_of_numbers:
            if num not in all_possible_sum:
                return num
    else:
        return 1


coins = [5, 7, 1, 1, 2, 3, 22]
#coins = [87]
#coins = [1, 2, 5]
#coins = [1, 1, 1, 1]

print(nonConstructibleChange(coins))
