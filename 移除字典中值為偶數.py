d = {"Jack": 60, "Tom": 80, "Iris": 45, "Ana": 70}
d1=d.copy()
for i in d1:
    if d[i] % 2 ==0:
        d.pop(i)
print(d)
    
