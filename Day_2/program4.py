# input() will always return a string data type

name = input("enter your name: ")

# get the first number from the user
number1 = int(input("Enter first number: "))

# get the second number from the user
number2 = int(input("Enter second number: "))

# add the two numbers
result = number1 + number2
print(f"hey {name}, result = {result}, data type = {type(result)}")