
days_list = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
input_first_day = "Sun"
# first day be on Thurs
 
is_first_day_set = False
date_order = []

for i in days_list:
    print(i, end=f"{' '*3}")

if input_first_day == "Mon":
    input_first_day_index = 1    
    # is_first_day_set = True
    
elif input_first_day == "Tue":
    input_first_day_index = 2
    # is_first_day_set = True
    
elif input_first_day == "Wed":
    input_first_day_index = 3
    # is_first_day_set = True
    
elif input_first_day == "Thu":
    input_first_day_index = 4
    # is_first_day_set = True
    
elif input_first_day == "Fri":
    input_first_day_index = 5
    # is_first_day_set = True
    
elif input_first_day == "Sat":
    input_first_day_index = 6
    # is_first_day_set = True
    
elif input_first_day == "Sun":
    input_first_day_index = 7
    # is_first_day_set = True
    
start_1stweek = 1
end_1stweek = (7 - (input_first_day_index)) + 1
# print(start_1stweek, end_1stweek)
list_1stweek = [i for i in range(start_1stweek, end_1stweek+1, 1)]
end_1stweek +=1
list_2stweek = [i for i in range(end_1stweek, end_1stweek+1+7)]
end_1stweek +=7
list_3stweek = [i for i in range(end_1stweek+1, end_1stweek+1+7)]
end_1stweek +=7
list_4stweek = [i for i in range(end_1stweek+1, end_1stweek+1+7) if i <= 31]
end_1stweek +=7
list_5stweek = [i for i in range(end_1stweek+1, end_1stweek+1+7) if i <= 31]

# print(list_1stweek, list_2stweek, list_3stweek, list_4stweek, list_5stweek)

days_list = [list_1stweek, list_2stweek, list_3stweek, list_4stweek, list_5stweek]

print()
for i in days_list:
    for j in i:
        if not is_first_day_set:
            print(f"{' '*4*6}", end= " ")
            is_first_day_set = True
        print(j, sep ="", end=f"{' '*4}")
    print()
    
    
# if is_first_day_set:
#     print(f"{' '*4}{j}", sep= " ", end= " ")


# input_last_day_index = input_first_day_index % 6
# arr1 = [i for i in range(1, input_last_day_index, 1)]



# is_first_day_set = False
# for j in range(1, 31, 1):
#     print()
#     if input_first_day == "Mon":
#         is_first_day_set = True
#         print(f"{' '*1}{j}", sep= " ", end= " ")
#     elif input_first_day == "Tue":
#         is_first_day_set = True
#         print(f"{' '*5}{j}", sep= " ", end= " ")
#     elif input_first_day == "Wed":
#         is_first_day_set = True
#         print(f"{' '*9}{j}", sep= " ", end= " ")
#     elif input_first_day == "Thu":
#         is_first_day_set = True
#         print(f"{' '*13}{j}", sep= " ", end= " ")
#     elif input_first_day == "Fri":
#         is_first_day_set = True
#         print(f"{' '*17}{j}", sep= " ", end= " ")
#     elif input_first_day == "Sat":
#         is_first_day_set = True
#         print(f"{' '*21}{j}", sep= " ", end= " ")
#     elif input_first_day == "Sun":
#         is_first_day_set = True
#         print(f"{' '*25}{j}", sep= " ", end= " ")
    
#     if is_first_day_set:
#         print(f"{' '*4}{j}", sep= " ", end= " ")
        

# print()
        
        

