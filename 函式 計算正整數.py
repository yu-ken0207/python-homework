def f(t,x):
    for i in x:
        if i==t:
            x.remove(i)
    return x
a = 3
b=[1,2,3,4]
print(f(a,b))
