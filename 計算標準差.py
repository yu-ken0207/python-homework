n=input("計算標準差")
all=()
start=0
end=0
for i in n:
  if i == " ":
      all = all + (n[start:end] , )
      start = end +1
      end =end+1
  else :
      end=end+1
a=0
for j in all:
   a=a+int(j)
   b=len(all)
c=int(a/b)
d=0
for k in all:
  d =d + round((int(k)-c)*(int(k)-c),2)

d=(d / 6) **0.5


print("標準差為:",round(d,2))
