
n = input("任意個1-10的整數")#1,3,2,3,5,6,4,3,7,4,5,7,8,4,2,10,5,2,9,3
n+=","
all=()
start=0
end=0
for i in n :
    if i == ",":
        all = all + (n[start:end] , )
        start = end +1
        end =end+1
    else :
        end=end+1
a=0
print(all)
a1=a2=a3=a4=a5=a6=a7=a8=a9=a10=0
alll=[]
for j in all:
        if int(j) == 1:
            a1+=1            
        elif int(j) == 2:
            a2+=1            
        elif int(j) == 3:
            a3+=1           
        elif int(j) == 4:
            a4+=1          
        elif int(j) == 5:
            a5+=1           
        elif int(j) == 6:
            a6+=1          
        elif int(j) == 7:
            a7+=1           
        elif int(j) == 8:
            a8+=1          
        elif int(j) == 9:
            a9+=1         
        elif int(j) == 10:
            a10+=1
alll.append(a1)
alll.append(a2)
alll.append(a3)
alll.append(a4)
alll.append(a5)
alll.append(a6)
alll.append(a7)
alll.append(a8)
alll.append(a9)
alll.append(a10)

print(alll)
