# using type hint feature to give a hint to the editor
num: int = 10
print(f"num = {num}, data type = {type(num)}")

# data type is inferred based on the value (string not an integer)
# the type hint feature is not useful here as the editor will 
# not be able to detect the error
name: int = "John"
print(f"name = {name}, data type = {type(name)}")