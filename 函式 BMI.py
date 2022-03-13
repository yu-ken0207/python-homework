def BMI(lenth,wei):
    ans = wei/((lenth/100)*(lenth/100))
    return(ans)
print("計算BMI")
lenth = int(input("輸入身高:"))
wei = int(input("輸入體重:"))
print(round(BMI(lenth,wei)),2)
