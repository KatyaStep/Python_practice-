def arrayOfProduct(array):
    product = [1] * len(array)
    for i in range(len(array)):
        running_product = 1
        for j in range(len(array)):
            if i != j:
                running_product *= array[j]
        product[i] = running_product

    return product
my_array = [5, 1, 4, 2]
# my_array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

arrayOfProduct(my_array)