n=int(input("輸入正整數"))
sum=0
for i in range (n,i-1):
  for j in range (1,i):
    print(j,"+",end= " ")
    sum=sum+j
  print()
print("全部=",sum)
