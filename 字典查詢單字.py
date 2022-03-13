print("字典查詢單字")
all=part=()

eng=""
while True:    
    eng = input("輸入英文單字")
    if eng  == "quit":
      print("輸入完成")
      break 
    chi = input("輸入中文翻譯")      
    part=()
    part=part+(eng,chi)    
    all = all + (part , )    
print(all)

while True:
        n = input('請輸入一個英文單字？')
        if n  == "quit":
            print("程式結束")
            break
        s=n.find(n)
        print(all[s][1])
    

