count=0
def prime(x):
    c =""
    b =()
    a=x.split()
    for i in a:        
        for j in range (2,int(i)):
            if int(i)== 2:
                b+= (i,)
                break
            if int(i) % int(j) == 0 :
                break
        else:
            b+= (i,)
    return b  
x = input("輸入:")
print(prime(x))

