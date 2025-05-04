import re

# findall
s = "Hello5 1111111111 world how are you hello again 1111"
p = re.findall("[0-9]{10}",s)
x = re.findall("[a-zA-Z0-9]+",s)
y = re.sub("\s","#",s)
print(y)

print(x)
y = re.sub("\s","",s)
print(y)
print(p)

