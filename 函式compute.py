def compute(a,b,c=1):
    sum=0
    
    for i in range (a,b,c):
        sum+=i
    return(sum)



print(compute(1,5))
