A1=input("溫度轉換，攝氏轉華氏輸入 1，華氏轉攝氏輸入 2:  ")

"華氏 = 攝氏*(9/5)+32"

"攝氏 = (華氏-32)*5/9"

num=int(A1)

if num <= 1 :
   P1=input("輸入溫度")
   P3=int(P1)
   print(float(P3*(9/5)+32))
   print("轉換完成")
   
if num > 1 :
    P2=input("輸入溫度")
    P4=int(P2)
    print(round(float((P4-32)*5/9),2))
    print("轉換完成")



