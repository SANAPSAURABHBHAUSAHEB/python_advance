from functions2 import is_prime, is_odd_or_even, factorial

# even_nos = [num for num in range(1, 100, 1) if is_odd_or_even(num)]
# print(f"All even in first 100 Natural Numbers --> {even_nos}")
#
# odd_nos = [num for num in range(1, 100, 1) if not is_odd_or_even(num)]
# print(f"All odd in first 100 Natural Numbers --> {odd_nos}")
#
# prime_nos = [num for num in range(1, 100, 1) if is_prime(num)]
# print(f"All prime in first 100 Natural Numbers --> {prime_nos}")

l = [10, 12, 68, 3, 2, 7, 9, 11, 56, 43, 67]

even_nos = [num for num in l if is_odd_or_even(num)]
print(f"All even in random list --> {even_nos}")

odd_nos = [num for num in l if not is_odd_or_even(num)]
print(f"All odd in random list --> {odd_nos}")

prime_nos = [num for num in l if is_prime(num)]
print(f"All prime in random list --> {prime_nos}")

# find a way to use fn in list comprehension
factorial_nos = [factorial(num) for num in l]
print(f"All factorial in random list --> {factorial_nos}")

str_names = ["Sriraj", "Ajinkya", "Aman", "Saurabh", "Aniket", "Rijul", "Arya", "Namoh", "Viraj", "Harsh", "Vipul", "Vertika"]

str_a = [name for name in str_names if name.lower().startswith("a")]
print(f"All names with a/A from list of names --> {str_a}")

vowels = ["a", "e", "i", "o", "u"]

def all_vowel(word: str) -> list:
    vowels = ["a", "e", "i", "o", "u"]
    vowels_in_word = []
    for str in word:
        if str in vowels:
            vowels_in_word.append(str)
    return vowels_in_word

def best_encrypt(lot_of_strings: str) -> str:
    vowels = ["a", "e", "i", "o", "u"]
    new_lot_of_strings = []
    for each_char in lot_of_strings:
        if not each_char.lower() in vowels:
            new_lot_of_strings.append(each_char)
            new_lot_of_strings.append("o")
            new_lot_of_strings.append(each_char)
        else:
            new_lot_of_strings.append(each_char)
    return "".join(new_lot_of_strings)


# str_a = [[name, all_vowel(name)] for name in str_names]
# print(f"All vowels in list of names --> {str_a}")
#
# str_a = [ for char_name in name if len(all_vowel(name)) > 1]
# print(f"All vowels in list of names --> {str_a}")

print(best_encrypt("This is Pluto, Namaste Earthlings!!! I am an Alien"))

list_of_random_berries = ["green grapes", "black grapes", "black berry", "red berry", "not a berry", "berry", "ber",
                          "plum", "cranberry"]

some_berries = [berries for berries in list_of_random_berries if len(berries) > 6]
print(f"{list_of_random_berries} --> {some_berries}")