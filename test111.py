print("AA")
a=0
b=0
c=0
d=0
e=0
f=0
n=1
while True:
    if n ==0:
        break
    n=int(input())
    
    b += 1
    a=(a+n)/b
    c=n-a
    d=c*c
    e=d+d
    f=(e**0.5)/b
print(f)
