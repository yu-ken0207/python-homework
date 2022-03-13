class student:                              #類別
    def init(self,I,n,h,e):                 #屬性
        self.ID =I                          #self=用來建立新的物件，radius=屬性名稱 0=粗使直
        self.name=n
        self.high=h
        self.eight=e
    def change_radius(self,I,n,h,e):        #定義方法
        self.ID =I                           
        self.name=n
        self.high=h
        self.eight=e
    def get(self):
        return (self.ID , self.name , self.high , self.eight)

    def get_BMI(self):
        return (round((self.eight/(self.high/100)**2),2))


a=student()
all=[[10814092,"游凱翔",170,56],[123,"John",180,80],[1234,"Mary",156,48],[8787,"Tom",168,45]]
bmi=[]
for i in all:
    a.change_radius(i[0],i[1],i[2],i[3])
    print(i[1],"BMI =",a.get_BMI())
    bmi+=[a.get_BMI(),]

    
bmi1=sorted(bmi,reverse=1)
print("bmi 最高者為",bmi1[0])

