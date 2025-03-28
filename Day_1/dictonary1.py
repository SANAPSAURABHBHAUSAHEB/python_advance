d1 ={1:"a",2:"b",3:"c",4:"d"}

print(d1[1])
print(d1.keys())
print(d1.values())
print(d1.items())
d1[1]= "z"
print(d1)
print(d1.pop(4))
for i in d1:
    print(i,d1[i])
   
    
