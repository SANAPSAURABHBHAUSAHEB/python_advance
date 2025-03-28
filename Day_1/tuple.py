a, b, c = [], [], []
for i in range(1, 101, 1):
    if i%2 ==0:
        a.append(i)
    else:
        b.append(i)
        is_prime = False
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
            else:
                is_prime = True
        if is_prime:
            c.append(i)
    # print(f"is num {i} prime ? {is_prime}")
print(a)
print(b)
print(c)

e , f, g =tuple(a), tuple(b), tuple(c)
print()
print(e)
print(f)
print(g)


r = "car"
r.replace(r[0], r[0].upper())