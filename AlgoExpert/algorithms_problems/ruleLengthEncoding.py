# def ruleLengthEncoding(string):
#     output = []
#
#     for i in range(len(string)):
#         if i != len(string)-1:
#             if string[i] != string[i+1]:
#                 countLetters(string[:i+1], string[i], output)
#         else:
#             countLetters(string[:i + 1], string[i], output)
#
#     # new_str = set(string)
#     #
#     # for letter in new_str:
#
#
#         # print(len(string))
#     print("".join(output))
#     return True


# def countLetters(string, letter, output):
#     counter_of_letter = string.count(letter)
#     if counter_of_letter > 9:
#         for i in range(counter_of_letter % 9):
#             output.append(str(9) + letter)
#         output.append(str(counter_of_letter % 9) + letter)
#     else:
#         output.append(str(counter_of_letter) + letter)
#
#     return output


def ruleLengthEncoding(string):
    counter = 0
    output = []

    for i in range(len(string)):
        if i != len(string)-1:
            if string[i] == string[i+1]:
                counter += 1
                if counter == 9:
                    output.append(str(counter) + string[i])
                    counter = 0
            else:
                counter += 1
                output.append(str(counter) + string[i])
                counter = 0
        else:
            counter += 1
            output.append(str(counter) + string[i])
            counter = 0

    print("".join(output))




# my_string = "************^^^^^^^$$$$$$%%%%%%%!!!!!!AAAAAAAAAAAAAAAAAAAA"
# my_string = "AAAAAAAAAAAAAAAAAAAA"
# my_string = "aAaAaaaaaAaaaAAAABbbbBBBB"
my_string = "AAAAAAAAAAAAABBCCCCDD"
ruleLengthEncoding(my_string)