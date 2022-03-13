a=int(input("輸入一個奇數n"))
b=1
P=0
for i in range (1,a+1,2):    
    P=P+(4/(i*b))
    b=-b
print(P)
