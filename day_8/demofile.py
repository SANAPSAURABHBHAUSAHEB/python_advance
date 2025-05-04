from day7.DessertItem import Candy

file = "abc.txt"

 

def copyData(fromfile1, tofile2):
    
    # Reading
    f = open(file= fromfile1, mode= "r")
    try:
        data=f.read()
    except Exception:
        print("Error while reading file")
    else:
        print(f"Data Read --> \n{data}")
    finally:
        f.close()
        
    # Writing
    f = open(file= tofile2, mode= "w")
    try:
        f.write(data)
    except Exception:
        print("Error while writing in file")
    else:
        print("Coping Data Successfull")
    finally:
        f.close()
        
def readData(fromfile1):
    data = ""
    # Reading
    f = open(file= fromfile1, mode= "r")
    try:
        data=f.read()
    except Exception:
        print("Error while reading file")
    else:
        print(f"Data Read --> \n{data}")
    finally:
        f.close()
        return data
        # pass
    
def writeData(tofile2, data= "default data"):
    
    # Writing
    f = open(file= tofile2, mode= "w")
    try:
        f.write(data)
    except Exception:
        print("Error while reading file")
    else:
        print(f"Data Saved")
    finally:
        # f.close()
        pass
    
def writeData2(tofile2, data= "default data"):
    
    # Writing
    f = open(file= tofile2, mode= "w")
    try:
        f.write(data)
    except Exception:
        print("Error while reading file")
    else:
        print(f"Data Saved")
    finally:
        f.close()
# capitaldata = " ".join([i.capitalize() for i in readData("abc.txt").split()])



data = readData(fromfile1="xyz.txt")
writeData(tofile2="xyz.txt", data= data)
writeData2(tofile2="xyz.txt", data= data)

candy = Candy("Candy", 2)
print(candy)

# print(f"Capitalize Data --> \n{capitaldata}")
    
        
# copyData(fromfile1= "abc.txt", tofile2="xyz.txt")
    


# with open(file= file, mode= "w") as f:
#     try:
#         f.write("hello world how are you where are you")
#     except Exception as e:
#         print(e)

# with open(file= file, mode= "a") as f:
#     try:
#         f.write("good morning")
#     except Exception as e:
#         print(e)
        

# with open(file= file, mode= "r") as f:
    
#     try:
#         print(f.read())
#     except Exception as e:
#         print(e)
        


# print=data


# f = open(file= file, mode= "w")
# try:
#     f.write("hello world how are you where are you")
# except Exception:
#     print("Error while writing in file")
# finally:
#     f.close()
    
# f = open(file= file, mode= "r")
# try:
#     data=f.read()
# except Exception:
#     print("Error while reading file")
# finally:
#     f.close()

