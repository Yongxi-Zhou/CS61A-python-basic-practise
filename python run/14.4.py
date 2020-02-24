import random
import time

# 创建一个类，可实例化成具体的游戏角色
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

    def K_buff(self,target):
        if target.name=='【暗影刺客】':
            self.attack=int(self.attack*1.5)
            print('【圣光骑士】对 【暗影刺客】说：“让无尽光芒制裁你的堕落！')

class Assassin(Role):
    def __init__(self, name='【暗影刺客】'):
        Role.__init__(self,name)
        self.life = self.life*3
        self.attack = self.attack*5

    def K_buff(self,target):
        if target.name=='【精灵弩手】':
            self.attack=int(self.attack*1.5)
            print('【暗影刺客】对 【精灵弩手】说：“主动找死，就别怪我心狠手辣。')

class Bowman(Role):
    def __init__(self, name='【精灵弩手】'):
        Role.__init__(self,name)
        self.life = self.life*4
        self.attack = self.attack*4

    def K_buff(self,target):
        if target.name=='【圣光骑士】':
            self.attack=int(self.attack*1.5)
            print('【精灵弩手】对 【圣光骑士】说：“骑着倔驴又如何？你都碰不到我衣服。')
        

        
# 创建一个类，可生成3V3并展示：可分为：欢迎语→随机生成→展示角色
class Game:
    def __init__(self):
        # 初始化各种变量
        self.players = []
        self.enemies = []
        self.round=1
        self.score = 0
        # 执行各种游戏函数
        self.game_start()
        self.born_role()
        self.show_role()
        self.order()
        self.pk_process()
        self.show_result

    # 欢迎语
    def game_start(self):
        print('------------ 欢迎来到“PK小游戏” ------------')
        print('将自动生成【玩家角色】和【电脑人物】')
        input('请按回车键继续。')
    
    # 随机生成6个角色
    def born_role(self):
        for i in range(3):
            self.players.append(random.choice([Knight(),Assassin(),Bowman()]))#随机的类不用加class，定义a= Knight()也不用加class
            self.enemies.append(random.choice([Knight(),Assassin(),Bowman()]))#list.append(列表中的元素)

    # 展示角色
    def show_role(self):
        print('----------------- 角色信息 -----------------')
        print('你的队伍：')
        for i in range(3):
            print( '『我方』%s 血量：%s  攻击：%s'%
            (self.players[i].name,self.players[i].life,self.players[i].attack))
        print('--------------------------------------------')

        print('敌人队伍：')
        for i in range(3):
            print('『敌方』%s 血量：%s  攻击：%s'%
            (self.enemies[i].name,self.enemies[i].life,self.enemies[i].attack))
        print('--------------------------------------------')

    def order(self):#用字典将出场数字和名字对应上
        self.player_dic1={}
        for i in range(3):
            self.order = int(input('你要把{}放在第几位？（请输入数字1,2,3)'.format(self.players[i])))
            self.player_dic1[self.order]=self.players[i]#用字典将出场数字和名字对应上
        print(self.player_dic1)
        self.players=[]
        #用字典键重新添加
        for i in range(1,4):
            self.players.append(self.player_dic1[i])#用新列表按顺序加名字,对应键值 1，2，3
        print(self.players)
    #print(self.player)#外部函数不能用内部的函数的变量

    def pk_process(self):
        for i in range(3):
            #加buff，实例.buff函数(攻击对象)
            self.players[i].K_buff(self.enemies[i])
            self.enemies[i].K_buff(self.players[i])

            #先定义几个变量
            self.player_name=self.players[i]
            self.robot_name=self.enemies[i].name
            self.player_life=self.players[i].life#将名字和血，攻击链接上
            self.player_attack=self.players[i].attack
            self.robot_life=self.enemies[i].life
            self.robot_attack=self.enemies[i].attack
            print('\n----------------- 【第{}局】 -----------------' .format(self.round))
            print('玩家角色：{} VS 敌方角色：{}'.format(self.player_name,self.robot_name))
            print('{}血量：{}  攻击：{}'.format(self.player_name,self.player_life,self.player_attack))
            print('{}血量：{}  攻击：{}'.format(self.robot_name,self.robot_life,self.robot_attack))
            time.sleep(2)

            while self.player_life>0 and self.robot_life>0:
                self.player_life=self.player_life-self.robot_attack
                self.robot_life=self.robot_life-self.player_attack
                print('{}发起攻击，{}剩余血量{}'.format(self.player_name,self.robot_name,self.robot_life))
                print('{}发起攻击，{}剩余血量{}'.format(self.robot_name,self.player_name,self.player_life))
                time.sleep(1.5)
            print(self.show_result(self.player_life,self.robot_life)[1])
            self.score+=self.show_result(self.player_life,self.robot_life)[0]
            print("第{}局player比分是{}".format(self.round,self.score))
            self.round+=1

        input=('点击回车查看结果')
        if self.score>=1:
            print('player win')
        elif self.score<0:
            print('robot win')
        else:
            print('Fair!')

    def show_result(self,player_life,robot_life):#要定义才能传递参数给上面
        if player_life>0 and robot_life<=0:
            #返回元组，记录（赢了还是输了，+-1）
            result='\n我赢了，电脑输了'
            return 1,result #返回元组的写法，多个返回值只能用元组
        elif robot_life>0 and player_life<=0:
            result='\n电脑赢了，我输了'
            return -1,result
        else:
            result='同归于尽'
            return 0,result

gp = Game()  # 运行游戏