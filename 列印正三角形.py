n=int(input("輸入正整數"))

for i in range(n):

    print(" "*(n-i),end="")
    print("*"*(2*i+1))
