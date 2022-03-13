import random
c=1
d=100
a=random.randint(1,100)
b=int(input("請猜1~100一個數字"))
while b>100 or b<1:
    b=int(input("請猜1~100一個數字"))
else:
    while a != b:
        if a>b:
            c=b+1
            b=int(input("請輸入"+str(c)+"到"+str(d)))
        else:
            d=b-1
            b=int(input("請輸入"+str(c)+"到"+str(d)))
if a==b:
    print("bingo")
    
        

