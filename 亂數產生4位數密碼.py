import random
a=random.randint(0,9999)
print(a)




for i in range (3):
  b=int(input("使用者輸入密碼"))
  if a != b:
      print("再輸入一次")
      
  else:
        b=int(input("正確"))
        break
else:
  print("3次錯誤,沒收卡片")       
                 

