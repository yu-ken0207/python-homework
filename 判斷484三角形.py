a=int(input("請輸入邊長"))
b=int(input("請輸入邊長"))
c=int(input("請輸入邊長"))
if (a+b)>c and (b+c)>a and (c+a)>b:
    if a==b==c:
        print("正三角形")
    elif a==b or b==c or c==a:
        print("等腰三角形")
    else:
        print("一般三角形")
else:
    print("不是三角形")
