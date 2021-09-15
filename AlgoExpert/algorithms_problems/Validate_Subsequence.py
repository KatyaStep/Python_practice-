# def isValidSequence(array, sequence):
#     if len(sequence) > 1:
#         for i in range(len(sequence)-1):
#             num = sequence[i]
#             if num in array:
#                 if array.index(num) >= array.index(sequence[i+1]):
#                     return False
#             else:
#                 return False
#     else:
#         if sequence not in array:
#             return False
#     return True


def isValidSequence(array, sequence):
    seaIdx = 0
    for num in array:
        if seaIdx == len(sequence):
            break
        if sequence[seaIdx] == num:
            seaIdx += 1

    return seaIdx == len(sequence)


array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [25]

print(isValidSequence(array, sequence))