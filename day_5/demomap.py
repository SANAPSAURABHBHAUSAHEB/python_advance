from functools import reduce

l = [10, 2, 34, 33, 12, 1, 8, 56, 4]
m = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = [1, 2, 3, 8, 9, 10, 12, 13, 14, 15]

def multiple(a):
    return a*a

def sum(a):
    return a+a

def divide(a):
    return a/a

def double(a):
    return a*2

def triple(a):
    return a*3

def myfunc(x):
    if x>10:
        return True
    else:
        return False

def add(a: int, b: int) -> int:
    # print("Annotations")
    # print(add.__annotations__)
    return a+b

x1 = list(map(multiple, l))
x2 = list(map(sum, l))
x3 = list(map(divide, l))
x4 = list(map(double, l))
x5 = list(map(triple, l))
x6 = list(map(lambda x: x*x, l))
x7 = list(map(lambda x: x+x, l))
x8 = list(map(lambda x: x/x, l))
x9 = list(map(lambda x: x*2,l))
x9 = list(map(lambda l, m: l*m, l, m))
x10 = list(map(lambda l, m, n: l+m+n, l, m, n))
x11 = list(filter(myfunc, l))
x12 = list(filter(lambda x: x>10, l))
x13 = reduce(add, l) # reduce takes two arguments and returns a single value


# common elements in both lists
x14 = list(filter(lambda x: x in l, m))
def myfunc(x):
    if x in l:
        return True
    else:
        return False

# x15


print(x1)
print(x2)
print(x3)
print(x4)
print(x5)
print(x6)
print(x7)
print(x8)
print(x9)
print(x10)
print(x11)
print(x12)
print(x13)
print(x14)
print(x14)

print(add(5, 6))