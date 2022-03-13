all="I have a pen. I have an apple. Apple pen. I have a pen. I have a pineapple. Pineapple pen."

p1=all.count("pen")
p2=all.count("apple")
p3=all.count("pineapple")

p4=all.count("Pen")
p5=all.count("Apple")
p6=all.count("Pineapple")

print("Pen有",p1+p4,"個,","Apple有",p2+p5,"個,","Pineapple有",p3+p6,"個")

all=all.replace ("pen","cat")
all=all.replace ("apple","orange")
all=all.replace ("pineapple","blueberry")

all=all.replace ("Pen","Cat")
all=all.replace ("Apple","Orange")
all=all.replace ("Pineapple","Blueberry")
print(all)




