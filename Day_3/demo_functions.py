
def hello():
    print("hello")

def add(a=0, b=0):
    return a+b

def even(a):
    return a%2==0

def odd(a):
    return a%2!=0

# def factorial(a):
#     fact = a
#     return fact*factorial(a-1)

def factorial(a):
    fact = a
    for i in range(2, a, 1):
        fact *= i
    return fact

def prime(a):
    is_prime = False
    for i in range(2, a):
        if a % i == 0:
            is_prime = False
            break
        else:
            is_prime = True
    return is_prime

def add1(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

def add2(arr):
    sum = 0
    if isinstance(arr, int):
        return arr
    elif isinstance(arr, list):
        for i in arr:
            sum += i
        return sum

# hello()
# print(add())
# print(add(a=30))
# print(add(b=21))
# print(add(a=18, b=29))
# print(add(a=23, b=12))
# print(add(a=17, b=21))
#
# print("args add", add1(1,2,3,4,5,5,6,6,6,6,6,6,6,6,6,6))
# print("add2", add2(1))
# print("add2", add2([1, 6, 7, 8]))
#
#
#
# print(f"is Even 17 --> {even(a=17)}")
# print(f"is Odd 17 --> {odd(a=17)}")
# print(f"Factorial 5 --> {factorial(a=5)}")
# print(f"is Prime 17 --> {prime(a=17)}")

hello()

reflect_x = lambda a:a

# print(reflect_x(1))