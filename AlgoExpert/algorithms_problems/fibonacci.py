def getNthFib(n):
    # fibonacci = [0, 1]
    #
    # for i in range(2, n+1):
    #     newNumber = fibonacci[i-1] + fibonacci[i-2]
    #     fibonacci.append(newNumber)
    #
    # print(fibonacci[n-1])

    if n == 2:
        return 1
    elif n == 1:
        return 0
    else:
        return getNthFib(n-1) + getNthFib(n-2)

print(getNthFib(6))