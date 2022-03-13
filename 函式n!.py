#1+1*2+1*2*3+1*2*3*4+....

def sum(a):
    b=1
    for i in range(1,a+1):
       b=b*i
    return b



n=int(input("輸入"))


b=0
for i in range (1,n+1):
    b =b +sum(n)
print(b)
