a=int(input("輸入三個數字"))
b=int(input("還有兩個數字"))
c=int(input("最後一個數字")) # 1 2 3

if a > b and a > c :
    if b > c:
        print(a,">",b,">",c)
    else :
        print(a,">",c,">",b)
elif b > a and b > c:
    if a > c:
        print(b,">",a,">",c)
    else:
        print(b,">",c,">",a)
elif c > a and c > b:
    if a > b :
        print(c,">",a,">",b)
    else:
        print(c,">",a,">",b)
print("完成!")
          
