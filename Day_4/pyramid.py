
total_rows = int(input("Enter Number of rows ")) #5
total_cols = (1 + (total_rows - 1)*2) #9 # applying AP

central_pt = total_cols//2
printing_indexes = [central_pt]

for i in range(0, total_rows, 1):
    for j in range(0, total_cols, 1):
        if i+j in printing_indexes:
            print(f"*", end="")
        else:
            print(" ", end="")
    print()
    last_index = printing_indexes[-1]
    printing_indexes.append(last_index+1)
    printing_indexes.append(last_index+2)