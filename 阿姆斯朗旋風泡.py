def arm(x):
    a=()
    x= str(x)
    for i in x:
        a=a+(int(i),)
    if int(x) == int(a[0])**3 + int(a[1])**3 + int(a[2])**3:
        return True
    else:
        return False   
x = int(input("輸入100-500正整數:"))
print(arm(x))
b=()
if arm(x):
    print("是阿姆斯壯數")
    for j in range(100,501):
        if arm(j):
          b+=(j,)
    print(b,"也是阿姆斯壯數")

        
else:
        print("不是阿姆斯壯數")
        
        

    
