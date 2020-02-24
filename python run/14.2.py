import random

class role():
    def __init__(self):
        self.name='normal'
        self.attack=random.randint(50,80)
        self.blood=random.randint(200,400)

class Knight(role):
    def __init__(self):
        self.name='骑士'
        self.attack=random.randint(50,80)*3
        self.blood=random.randint(200,400)*5
        print('{}\n血量:{}\n攻击：{}'.format(self.name,self.blood,self.attack))

class Assassin(role):
    def __init__(self):
        self.name='杀手'
        self.attack=random.randint(50,80)*5
        self.blood=random.randint(200,400)*3
        print('{}\n血量:{}\n攻击：{}'.format(self.name,self.blood,self.attack))

class Bowman(role):
    def __init__(self):
        self.name='射手'
        self.attack=random.randint(50,80)*4
        self.blood=random.randint(200,400)*4
        print('{}\n血量:{}\n攻击：{}'.format(self.name,self.blood,self.attack))

#game=Game()
knight=Knight()#继承后，实例化的函数不加父类名字 #Assassin=Assassin(role)错的
Assassin=Assassin()
Bowman=Bowman()