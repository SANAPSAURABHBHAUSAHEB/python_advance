
str_input1 = "the_new_class"

str_input1_list = str_input1.split("_")
str_input2_list = []

for i in str_input1_list:
    str_input2_list.append(i.capitalize())
    
conv_str_input1 = "".join( str_input2_list)
print(f"{str_input1} ==> {conv_str_input1}")

