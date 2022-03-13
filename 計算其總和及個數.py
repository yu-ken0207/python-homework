count=0
sun=0
while True:
    a=int(input("輸入不定個數之正整數"))
    sun=sun+a
    count=count+1
    if a == -1 :
        break
print("總和=",str(sun),"個數 =",str(count))
