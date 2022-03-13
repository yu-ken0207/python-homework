p1=input("姓名:")
p2=input("身高:")
p3=input("體重:")

bmi=float(p3)/((int(p2)/100)*(int(p2)/100))
print(p1,"身高",p2,"公分,","體重",p3,"公斤,","BMI質",round(bmi,2))
