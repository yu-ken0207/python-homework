class Rectangle:
    def _init_(self,l,w):
        self.length = l
        self.width = w
    def change_radius (self,l,w):
        self.length=l
        self.width=w
    def get_area(self):
        self.area=self.length*self.width
        return (self.area)
    def get_perimeter(self):
        self.perimeter=2*self.length+2*self.width
        return (self.perimeter)
    def get(self):
        return (self.length,self.width)
p=Rectangle()
p.change_radius(4,2)
print(p.get_area())

