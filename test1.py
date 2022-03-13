#move=''
#while move not in '1 2 3 4 5 6 7 8 9'.split():

        #print("What is your next move?(1-9)")
        #move = input()
#print(move)


n=1
y=0
t=[2,3,10]
while y!=1:
    while  n in t:
        print(1)
        y=2
    else:
        print(2)
        t.append(n)
        y=1

#for j in range (0,len(t)) :
    #for i in t :
        #if n == t[j]:
            #print(1)
            #break
        #else :
            #print(2)
            #break

def 判斷(m):
    while m in z:
        n=input("x:")
        return n
    else:
        z.append(m)
        return 
