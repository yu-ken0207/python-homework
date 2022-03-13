b = {"milk": 2, "apple": 5, "bread": 2, "banana": 4}
d = {"apple": 1, "banana": 4}
c=list(b)
print(b)
for i in c:
    for j in d:
        if i == j:
            b[i]=b[i]-int(d[i])
            if b[i] == 0:
                b.pop(i)
        
print(b)

  
