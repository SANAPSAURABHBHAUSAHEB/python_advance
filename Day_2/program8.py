# empty function
# - function without a body

# function declaration + definition
# function which has only one statement as pass statement   
def empty_function():
    pass

# function call
# empty_function()

# parameterless function
# function without any parameters
def function1():
    print("inside function1")
    number1 = int(input("Enter first number: "))
    number2 = int(input("Enter second number: "))
    result = number1 + number2
    print(f"result = {result}")

# function call
# function1()

# parameterized function
# function with at least one parameter
# int function2(int param) {...}
def function2(param):
    print("inside function2")
    print(f"param = {param}, type = {type(param)}")

# param here is of type int

# indexed parameters
# function2(10)

# named parameters
# function2(param=10)

# param here is of type float
# function2(15.50)
# function2(param=15.50)

# param here is of type string
# function2("test")
# function2(param="test")

# param here is of type boolean
# function2(True)
# function2(param=True)


def function3(p1, p2):
    print("inside function3")
    print(f"p1 = {p1}, type = {type(p1)}")
    print(f"p2 = {p2}, type = {type(p2)}")
    result = p1 + p2
    print(f"result = {result}")

# indexed parameters
# function3(10, 20)
# function3(20, 10)

# since, p2 is missing, this will raise an error
# function3(10)

# named parameters
# function3(p1=10, p2=20)
# function3(p2=20, p1=10)

# mixed parameters
# function3(10, p2=20)

# since, p1 is getting multiple values, this will raise an error
# function3(10, p1=20)

# since, it is invalid to use indexed parameters after named ones this will raise an error
# function3(p1=10, 20)


def function4(name, address, age, salary):
    print("inside function4")
    print(f"name = {name}, type = {type(name)}")
    print(f"address = {address}, type = {type(address)}")
    print(f"age = {age}, type = {type(age)}")
    print(f"salary = {salary}, type = {type(salary)}")

# function4("John", "Pune", 30, 15.50)
# function4(name="John", address="Pune", age=30, salary=15.50)

def function5():
    """this is a docstring of function5"""
    print("inside function5")

# dunder attribute
# print(f"docstring of function5 = {function5.__doc__}")
# print(print.__doc__)
# print(int.__doc__);