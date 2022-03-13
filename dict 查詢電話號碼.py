n=""
data={}
while True:    
    n=input("輸入姓名，輸入quit離開")
    if n== "quit":
        break
    n1=input("輸入電話")
    
    data[n]=n1
    print(data)
while True:    
    n2=input("查詢資料，輸入quit離開")
    if n2== "quit":
        break
    for i in data:
        if n2 == i :
            print(data[n2])
            break
            
    else:
            print("查無此人")
            
