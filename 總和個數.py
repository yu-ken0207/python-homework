i=0
sum=0
while True:
    a=int(input("請輸入一個正整數或-1離開"))
    if a ==-1:
        break
    sum=sum+a
    i+=1
print("總和="+str(sum))
print("個數="+str(i))
