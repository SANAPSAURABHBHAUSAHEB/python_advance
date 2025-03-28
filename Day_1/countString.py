string_1= " hello world welcome hello world welcome hello world welcome hello world welcome"

string_1 = string_1.strip()
string_lst = string_1.split(" ")
print()

sub_str_count_lst = []
sub_str_count_lst_2 = []

for i in string_lst:
    sub_str_count = string_1.count(i)
    print(f"{i} --> {sub_str_count}")
    
    sub_str_count_lst.append([i, sub_str_count])
    
print(sub_str_count_lst)

for i in sub_str_count_lst:
    if not i in sub_str_count_lst_2:
        sub_str_count_lst_2.append(i)
        
print(sub_str_count_lst_2)
