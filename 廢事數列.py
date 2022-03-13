A=int(input("輸入數值"))
A1=0
B2=1
s=()
c=0
for i in range(1,A):
    c=A1+B2
    A1=B2
    B2=c
    s=s+(c,)
print(s)
