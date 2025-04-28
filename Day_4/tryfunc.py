

from functions2 import is_prime, is_odd_or_even, factorial


num = int(input("Enter a Number ::: "))

if is_prime(num):
    print(f"{num} --> Prime number")
else:
    print(f"{num} --> Not a Prime number")

if is_odd_or_even(num):
    print(f"{num} --> Even number")
else:
    print(f"{num} --> Odd number")

print(f"Factorial of {num} --> {factorial(num)}")