def sum(a,b,c=0):
    
    all=0
    all = a*b
    if a >= 100:
        all +=1000
    return all
   
    



t = (('John', 80, 150), ('Mary', 100, 150), ('Python', 50, 200))  
print("John=",sum(t[0][1],t[0][2]))
print( "Mary=",sum(t[1][1],t[1][2]))
print("Python=",sum(t[2][1],t[2][2]))

a=sum(t[0][1],t[0][2])
b=sum(t[1][1],t[1][2])
c=sum(t[2][1],t[2][2])
print("Total=" ,(a+b+c))
