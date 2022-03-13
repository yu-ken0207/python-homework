s = "Aqua Man"
m = s[:s.find(" ")]


a=s[0:int(len(m)/2)]    

b=s[int(len(m)/2)  : len(m)]  

c= int(len(s[s.find(" ")+1:s.rfind("")])/2)

c1=s[s.find(" ")+1:s.rfind("")]

c2=int(len(s[s.find(" ")+1:s.rfind("")])/2)

c3 =c1[:c2]               

c4 = c1 [c2:]           



print(a,b,c3,c4)


s2= "Cat Woman"

m1=s2[:s2.find(" ")]

a1=s2[0:int(len(m1)/2)]   

b1=s2[int(len(m1)/2)  : len(m1)]

c1= int(len(m1[s2.find(" ")+1:s2.rfind("")])/2)

c11=s2[s2.find(" ")+1:s2.rfind("")]

c22=int(len(s2[s2.find(" ")+1:s2.rfind("")])/2)

c33 =c11[:c22]

c44 = c11 [c22:]

print(a1,b1,c33,c44)


name1=(a,b1,c3,c44)
name2=(a1,b,c33,c4)


print(name1)
print(name2)


