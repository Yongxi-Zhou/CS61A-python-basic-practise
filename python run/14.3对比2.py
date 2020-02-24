import random
class Role():
    def __init__(self, name='【角色】'):  # 把角色名作为默认参数
        self.name = name
        self.life = random.randint(100,150)
        self.attack = random.randint(30,50)
# 创建三个子类，可实例化为3个不同类型的角色
class Knight(Role):
    def __init__(self, name='【圣光骑士】'):   # 把子类角色名作为默认参数
        Role.__init__(self,name)  # 利用了父类的初始化函数
        self.life = self.life*5  # 骑士有5份血量
        self.attack = self.attack*3    # 骑士有3份攻击力
        print('{}\n血量:{}\n攻击：{}'.format(self.name,self.life,self.attack))

class Assassin(Role):
    def __init__(self,name="杀手"):
        Role.__init__(self,name)
        self.life=self.life*3
        self.attack=self.attack*5
        print('{}\n血量:{}\n攻击：{}'.format(self.name,self.life,self.attack))

class Bower(Role):
    def __init__(self,name='射手'):
        Role.__init__(self,name)
        self.life=self.life*4
        self.attack=self.attack*4
        print('{}\n血量:{}\n攻击：{}'.format(self.name,self.life,self.attack))

骑士=Knight()
杀手=Assassin()
射手=Bower()
print(骑士.attack)