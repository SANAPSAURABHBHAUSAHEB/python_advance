import string

# str_pangram = """The quick brown fox jumps over the lazy dog"""
str_pangram = """The quick brown fox dog"""

alphabet_list = list(string.ascii_lowercase)
# print(alphabet_list)

str_pangram_lst = str_pangram.strip().split(" ")
str_pangram_lst2 = "".join(str_pangram_lst).lower()

char_list = list(set(str_pangram_lst2))


for i in alphabet_list:
    is_match = False
    for j in char_list:
        # print(i, j, i==j)
        if i == j:
            is_match=True
            break
    if not is_match:
        print(f"Not a Pangram :: {str_pangram}")
        break
else:
    if is_match:
        print(f"Pangram Found :: {str_pangram}")
