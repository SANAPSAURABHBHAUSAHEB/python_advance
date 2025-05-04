file = "resourceblockcheck.txt"
with open(file= file, mode= "w+") as f:
    try:
        f.write("hello world how are you where are you")
    except Exception as e:
        print(e)

with open(file= file, mode= "a") as f:
    try:
        f.write("good morning")
    except Exception as e:
        print(e)
        

with open(file= file, mode= "r") as f:
    
    try:
        print(f.read())
    except Exception as e:
        print(e)
        