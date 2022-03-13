def find_word(d): 
    a=d.lower().split(" ")

    b=[]
    c=[]
    d=[]


    for i in a:
        b+=i.split(',')
    for j in b: 
        c+=j.split('.')
    for k in c:
        d+=k.split('!')

    for j in d:
        if j =="":
            x=d.index(j)
            d.pop(x)
    return d


d="I have a pen, I have an apple. Apple pen! I have a pen, I have a pineapple. Pineapple pen!"


find_word(d)

e={}

for m in find_word(d):
    if m in e:
        e[m]+=1
    else:
        e[m]=1
ek = []
key = list([i for i in e])
for i in sorted(e.values(),reverse=1):
    for k in e.keys():
        if e[k] == i and (k in key):
            ek += [(k,e[k]),]
            key.remove(k)



print(ek)


#print(sorted(e.values(),reverse=1))








