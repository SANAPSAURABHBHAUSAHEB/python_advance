file = "pqr.txt"
 # Writing
f = open(file=  "pqr.txt", mode= "r")
try:
    wordscount=f.read()
    
except Exception:
    print("Error while writing in file")
else:
    print("Coping Data Successfull")
finally:
    f.close()
    
liofch=["\n", ",","."]
liswors=wordscount.split(" ")

for i in liofch :    
    if i in liswors:
        liswors.remove(i)

print(liswors)

