t = [60, 76, 85, 43, 66, 92, 88, 75, 95, 80]
t.sort(reverse=True)
import math
a=len(t)/100*25
n=math.ceil(a)
tt=[]


for i in range(0,n):
    tt.append(t[i])

sum=0
for j in tt:
    sum+=j
b=sum / n
print(round(b,0))   


#第二種作法
#import math
#t1 = [60, 76, 85, 43, 66, 92, 88, 75, 95, 80]
#t1.sort()
#n1 = math.ceil(len(t1)*0.75)-1
#avg=sum(t1[n1:])/len(t1[n1:])
#print(avg)
