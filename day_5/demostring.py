
s = "Hello world how are you"

s_list = s.split(" ")

print(s_list)

s1 = list(map(lambda x: x.upper(), s_list))
s2 = list(map(lambda x: x.lower(), s_list))
s3 = list(map(lambda x: len(x), s_list))

s4 = list(zip(s1, s2, s3))
s5 = list(map(lambda x, y, z: [x , y, z], s1, s2, s3))

print(s4)
print(s5)
