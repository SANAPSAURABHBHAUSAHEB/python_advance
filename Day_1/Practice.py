p=[1,22,1,22,3,4,5,5,6]

for i in p:
  if p.count(i)>=2:
   p.remove(i)
   
print(p)
