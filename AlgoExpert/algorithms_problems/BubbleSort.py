def bubbleSort(array):
    isSorted = False
    while not isSorted:
        isSorted = True
        for i in range(len(array)-1):
            first_num = array[i]
            second_num = array[i+1]
            if first_num > second_num:
                array[i], array[i+1] = second_num, first_num
                isSorted = False
    print(my_array)
    return True

my_array = [8, 5, 2, 9, 5, 6, 3]
bubbleSort(my_array)