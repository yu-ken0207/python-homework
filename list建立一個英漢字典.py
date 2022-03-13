n=""
data={}
data1={}
print("輸入建立一個英漢字典")
while True:    
    n=input("輸入英文，輸入quit離開")
    if n== "quit":
        break
    n1=input("輸入中文，輸入quit離開")
    
    data[n]=n1
    print(data)


a=list(data)
print(a)
for i in a:
    data1[data[i]]=i
print(data1)


