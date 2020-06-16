def collatz(number):
    if number % 2 == 0:
        result = number // 2
        print (result)
        return result
    elif number % 2 == 1:
        result =  3 * number + 1
        print (result)
        return result
    else:
        return None

while True:
    print ('Enter a number:')
    
    try:
        number = int(input())
        result = collatz(number)

        if result == 1:
            break 

        continue
    except ValueError:
        print("The number must be integer")