class Animal():
    def __init__(self,name='动物'):    
        self.name=name
        self.attack=100

class Cat(Animal):
    def __init__(self,name="猫"):#如果要改变参数，先取代第一句，再引用父类的第二句
        Animal.__init__(self,name)

    def buff(self,mice):
        if mice.name=='老鼠':
            self.attack=int(self.attack*1.5)

class Rat(Animal):
    def __init__(self,name='老鼠'):
        Animal.__init__(self,name)#引用第二句要打(self,name)参数

Jerry=Rat()
Tom=Cat()
print(Tom.attack)
Tom.buff(Jerry)
print(Tom.attack)