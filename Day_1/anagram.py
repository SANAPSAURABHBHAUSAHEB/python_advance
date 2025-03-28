
str_input1 = "abcd"
str_input2 = "abdd"

# remove duplicates
str_input1 = "".join(set(str_input1))
str_input2 = "".join(set(str_input2))

if len(str_input1) == len(str_input2):
    is_match = False
    for i in str_input1:
        for j in str_input2:
            print(i, j, i==j)
            if i == j:
                is_match = True
                break
    if not is_match:
        print(f"Not an Anagram {str_input1} <--> {str_input2}")
    else:
        print(f"An Anagram {str_input1} <--> {str_input2}")
else:
    print(f"Not an Anagram {str_input1} <--> {str_input2}")    
    
                
            

