
# Primitive Arithmetic Exception Handling

# 9/0 :: ZeroDivisionError: division by zero
a1 = 9
a2 = 0

try:
    
    a = a1/a2
    print(f"a2 : {a2}")
except ZeroDivisionError: 
    print("a2 is zero, give a value greater than zero")
else:
    print(a)
finally:
    print("this will always execute")
    
    



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
    # try except
l1 = [1,2,3,3]
mun = 10
try:
    num>len(l1)
    print(l1[10])
except IndexError:
    print("index out of range")
finally:
    print("this will always execute ")
    
    text1="a"
    text2= 12
try:
    text1 = text1 + text2
except :
    print("check types")
finally:
    print("this will always execute")
    
    class MyException(Exception):
        def __init__(self,message="something went wrong"):
            self.message= message
            a=12
            if a >5:
             raise MyException("Value is grater than 5")