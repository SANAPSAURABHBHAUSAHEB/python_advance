# type conversion
# int(): converts the value to an integer
# float(): converts the value to a float
# bool(): converts the value to a boolean
# str(): converts the value to a string

# everything to integer
salary = 15.50
salary_int = int(salary)
print(f"salary = {salary}, data type = {type(salary)}")
print(f"salary_int = {salary_int}, data type = {type(salary_int)}")

# bool True => 1 in integer, False => 0 in integer
is_active = False
is_active_int = int(is_active)
print(f"is_active = {is_active}, data type = {type(is_active)}")
print(f"is_active_int = {is_active_int}, data type = {type(is_active_int)}")

# string to integer
num = "100"
num_int = int(num)
print(f"num = {num}, data type = {type(num)}")
print(f"num_int = {num_int}, data type = {type(num_int)}")

# this statement will raise an error
# num2 = "test"
# num2_int = int(num2)
# print(f"num2 = {num2}, data type = {type(num2)}")
# print(f"num2_int = {num2_int}, data type = {type(num2_int)}")

print('-' * 50)

# everything to float
num = 100
num_float = float(num)
print(f"num = {num}, data type = {type(num)}")
print(f"num_float = {num_float}, data type = {type(num_float)}")

# bool True => 1.0 in float, False => 0.0 in float
is_active = False
is_active_float = float(is_active)
print(f"is_active = {is_active}, data type = {type(is_active)}")    
print(f"is_active_float = {is_active_float}, data type = {type(is_active_float)}")

# string to float
salary = "15.50"
salary_float = float(salary)
print(f"salary = {salary}, data type = {type(salary)}")
print(f"salary_float = {salary_float}, data type = {type(salary_float)}")

# this statement will raise an error
# my_var = "test"
# my_var_float = float(my_var)
# print(f"my_var = {my_var}, data type = {type(my_var)}")
# print(f"my_var_float = {my_var_float}, data type = {type(my_var_float)}")

print('-' * 50)

# everything to boolean

# 0 => False, other than 0 => True
num = 0
num_bool = bool(num)
print(f"num = {num}, data type = {type(num)}")
print(f"num_bool = {num_bool}, data type = {type(num_bool)}")

# string to float

# empty string => False, other than empty string => True
my_val = "t"
my_val_bool = bool(my_val)
print(f"my_val = {my_val}, data type = {type(my_val)}")
print(f"my_val_bool = {my_val_bool}, data type = {type(my_val_bool)}")

print('-' * 50)


# everything to string
num = 100
num_str = str(num)
print(f"num = {num}, data type = {type(num)}")
print(f"num_str = {num_str}, data type = {type(num_str)}")