# import string

# lower_alphabet_list = list(string.ascii_lowercase)
# upper_alphabet_list = list(string.ascii_uppercase)


crypt_string = "pnrfne"
crypt_string_mappings = {"p": "c", "n": "a", "r": "e", "f": "s", "e": "r"}


for i in crypt_string:
    for j in crypt_string_mappings:
        if i == j:
            print(crypt_string_mappings[i], end="")