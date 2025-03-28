
dictionary_names_color = {"Atul": "Red", "Amit": "green", "Pooja": "Blue"}

dictionary_names_color_sorted = {}

temp = list(dictionary_names_color.keys())
temp.sort()

dictionary_names_color_sorted = dictionary_names_color_sorted.fromkeys(temp)
print(dictionary_names_color_sorted)

for i in temp: 
    dictionary_names_color_sorted[i] = dictionary_names_color[i]
        
        
print(dictionary_names_color_sorted)