# Write a function that takes a list value as an argument and returns a string 
# with all the items separated by a comma and a space, with and inserted before 
# the last item. 
# For example, passing the previous spam list to the function would 
# return 'apples, bananas, tofu, and cats'. But your function should be able to work 
# with any list value passed to it. Be sure to test the case where an empty list [] 
# is passed to your function.

def comma_code(list_value):
    new_str = ''

    if len(list_value) == 0:
        return (print ('Your list is empty'))
    else:
        for item in range(len(list_value)):
            if item < (len(list_value)-1):
                new_str += (list_value[item] + ', ')
            else:
                new_str += ('and ' + list_value[item])
    return (print(new_str))

list_value = ['banana', 'apple', 'peach']
#list_value = []

comma_code(list_value)