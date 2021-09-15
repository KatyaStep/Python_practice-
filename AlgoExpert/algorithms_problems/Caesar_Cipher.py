from string import ascii_lowercase

def caesarCioherEncryptor(string, key):
    alphabet = list(ascii_lowercase)
    new_string = []
    for i in range(len(string)):
        idx = alphabet.index(string[i])
        new_idx = (idx+key) % len(alphabet)
        new_string.append(alphabet[new_idx])

    print("".join(new_string))
    return string

# my_string = "xyz"
my_string = "abc"

caesarCioherEncryptor(my_string, 52)