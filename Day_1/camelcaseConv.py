import re

str_input1 = "TheNewClass"

print(re.split("[A-Z]", str_input1, maxsplit=0, flags=0))

import string
alphabet_list = list(string.ascii_uppercase)

for i in str_input1:
    for j in alphabet_list:
        pass

