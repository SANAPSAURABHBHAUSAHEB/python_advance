
# a1 = [1, 2, 3, 4, 4, 4, 7, 2, 4, 3, 1, 1, 1, 9, 9]
a1 = ["hello", "world", "how", "are", "world", "how", "are", "world", "how", "are", "world"]

a1_dictionary = {}

# for i in a1:
#     a1_dictionary[i] = i

a1.sort()
print(a1)

for i in a1:
    a1_dictionary[i] = a1.count(i)
    
# a1_dictionary.
    
    
print(a1_dictionary)
# print(a1_dictionary.values())

value_list = list(a1_dictionary.values())
value_list.sort()

a2_dictionary = {}
for i in value_list:
    for j in a1_dictionary:
        if i == a1_dictionary[j]:
            a2_dictionary[j] = i
        
print(a2_dictionary)