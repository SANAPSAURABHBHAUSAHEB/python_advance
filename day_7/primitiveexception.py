
# Primitive Arithmetic Exception Handling

# 9/0 :: ZeroDivisionError: division by zero
a1 = 9
a2 = 0

if not a2 == 0:
    a = a1/a2
    print(f"a2 : {a2}")
else:
    print("a2 is zero, give a value greater than zero")


# type error :: TypeError: can only concatenate str (not "int") to str
a1 = "Car"
a2 = 22

if isinstance(a1 , int) and isinstance(a2 , int):
    print(a1 + a2)
else:
    print("Types of the given variable are not matching")
    

# a[]:: IndexError: list index out of range
a1 = [3, 5, 6, 3, 8, 9, 3]
ind = 10

if ind <= len(a1):
    print(a1[10])
else:
    print("Array do not have a value in given index")