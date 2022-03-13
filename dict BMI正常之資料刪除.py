d = {"Jack": [165,60], "Tom": [180,80], "Iris": [170,45], "Ana": [200,70]}
d1=d.copy()
print(d1)
for l in d1:
    bmi=0
    bmi=round(d[l][1]/((d[l][0]/100)*(d[l][0]/100)),2)
    d[l]=d[l][0],d[l][1],bmi
    if bmi >=18.5 and bmi <24:
        d.pop(l)
    
print(d)


