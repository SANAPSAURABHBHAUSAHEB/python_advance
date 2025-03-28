a = [1,2,3]
b = [2,1,3]
row_num = 0
for i in range(0,len(a),1):
    isAMatch = False
    for j in range(0,len(b)):
        if len(a)==len(b):
            # print(a[i], b[j])
            if a[i]==b[j]:
                isAMatch = True
                print(a[i], b[j], "match")
            else:
                print(a[i], b[j], "not match")
                
        if isAMatch:
            break
        else:
            row_num+=1
if isAMatch:
    print(f"Two arrays is equal {a}, {b}")
else:
    print(f"Two arrays is notequal {a}, {b}")
      