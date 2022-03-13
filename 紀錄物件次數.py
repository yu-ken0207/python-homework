a="1,3,2,2,1,3,4,5"
c=a.split(",")

print(c)
b={}
for i in c:
    if i in b :
        b[i]+=1
    else:
        b[i]=1
    
print(b)
