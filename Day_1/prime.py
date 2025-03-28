
num = 45
is_prime = False

for i in range(2, num):
    if num % i == 0:
        is_prime = False
        break
    else:
        is_prime = True

print(f"is num {num} prime ? {is_prime}")