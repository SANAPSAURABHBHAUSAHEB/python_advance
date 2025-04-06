# declare a variable

# integer data type
num = 100
num = 200
num2 = num

# f here means the string is formatted
# type() is a built-in function that returns the data type of the variable
print(f"num = {num}, data type = {type(num)}")

# float data type
salary = 15.50
print(f"salary = {salary}, data type = {type(salary)}")

# string data type
# single line value
first_name = "John"
print(f"name = {first_name}, data type = {type(first_name)}")
first_name = 'amit'
print(f"name = {first_name}, data type = {type(first_name)}")

first_name2 = first_name

nick_name = "amit"

# string data type
# single line value
last_name = 'Doe'
print(f"last_name = {last_name}, data type = {type(last_name)}")

# string data type
# multi-line value
address1 = """H-105,
Pune, 
Maharashtra,
411041"""
print(f"address1 = {address1}, data type = {type(address1)}")

# multi-line value
address2 = '''H-105,
Pune, 
Maharashtra,
411041'''
print(f"address2 = {address2}, data type = {type(address2)}")

# boolean data type
is_active = True
print(f"is_active = {is_active}, data type = {type(is_active)}")

# complex data type
complex_num = 5 + 3j
print(f"complex_num = {complex_num}, data type = {type(complex_num)}")

num = "test"
print(f"num = {num}, data type = {type(num)}")

num = True
print(f"num = {num}, data type = {type(num)}")
