o = 'o'
x = 'x'
e = '_'
b = [ [ e, e, e], [e, e, e], [e, e, e] ]

def print_board(a=0,c=0):
    if a == "1":
        b[0][0]="x"
    if a == "2":
        b[0][1]="x"
    if a == "3":
        b[0][2]="x"
    if a == "4":
        b[1][0]="x"
    if a == "5":
        b[1][1]="x"
    if a == "6":
        b[1][2]="x"
    if a == "7":
        b[2][0]="x"
    if a == "8":
        b[2][1]="x"
    if a == "9":
        b[2][2]="x"


    if c == "1":
        b[0][0]="o"
    if c == "2":
        b[0][1]="o"
    if c == "3":
        b[0][2]="o"
    if c == "4":
        b[1][0]="o"
    if c == "5":
        b[1][1]="o"
    if c == "6":
        b[1][2]="o"
    if c == "7":
        b[2][0]="o"
    if c == "8":
        b[2][1]="o"
    if c == "9":
        b[2][2]="o"
    
    for i in b :
        print(i)

def check_board():
    if b[0][0]==b[0][1]==b[0][2]=="o":        
        print("o win , game over!")
        return True        
    if b[1][0]==b[1][1]==b[1][2]=="o":        
        print("o win , game over!")
        return True 
    if b[2][0]==b[2][1]==b[2][2]=="o":        
        print("o win , game over!")
        return True 
        
    if b[0][0]==b[1][0]==b[2][0]=="o":        
        print("o win , game over!")
        return True 
    if b[0][1]==b[1][1]==b[2][1]=="o":        
        print("o win , game over!")
        return True 
    if b[2][0]==b[2][1]==b[2][2]=="o":        
        print("o win , game over!")
        return True 
        
    if b[0][0]==b[1][1]==b[2][2]=="o":        
        print("o win , game over!")
        return True 
    if b[0][2]==b[1][1]==b[2][0]=="o":        
        print("o win , game over!")
        return True 

    ###################################
    if b[0][0]==b[0][1]==b[0][2]=="x":        
        print("x win , game over!")
        return True 
    if b[1][0]==b[1][1]==b[1][2]=="x":        
        print("x win , game over!")
        return True 
    if b[2][0]==b[2][1]==b[2][2]=="x":        
        print("x win , game over!")
        return True 
        
    if b[0][0]==b[1][0]==b[2][0]=="x":        
        print("x win , game over!")
        return True 
    if b[0][1]==b[1][1]==b[2][1]=="x":        
        print("x win , game over!")
        return True 
    if b[2][0]==b[2][1]==b[2][2]=="x":        
        print("x win , game over!")
        return True 
        
    if b[0][0]==b[1][1]==b[2][2]=="x":        
        print("x win , game over!")
        return True 
    if b[0][2]==b[1][1]==b[2][0]=="x":        
        print("x win , game over!")
        return True
    

    




z=[]
y=0
sum = 1
for i in b :
        print(i)
while True:    
    n=n1=0
    n=input("x:")
    y=0
    while y!=1:
        y=0
        while n in z:
            n=input("x:")
            y=0
        else:
            z.append(n)
            y=1
        

    
    n=print_board(n,n1)
    if check_board():
        break
    sum +=1
    if sum >= 9:
        print("和局")
        break
        
    n1=input("o:")
    y=0
    while y!=1:
        y=0
        while n1 in z:
            n1=input("o:")
            y=0
        else:
            z.append(n1)
            y=1
    



    
    n1=print_board(n,n1)
    sum +=1
    if check_board():
        break
    
