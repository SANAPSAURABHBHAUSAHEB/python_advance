a = [i for i in range(0, 101, 1) if i%2 !=0]
print(a)

a = []
for i in range(0, 101, 1):
    is_prime = False
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break
        else:
            is_prime = True
    if is_prime:
        a.append(i)
    # print(f"is num {i} prime ? {is_prime}")
print(a)