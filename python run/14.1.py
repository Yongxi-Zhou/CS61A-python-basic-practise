import random,time
class Game():
    player_list =  ['【狂血战士】','【森林箭手】','【光明骑士】','【独行剑客】','【格斗大师】','【枪弹专家】']
    enemy_list = ['【敌-暗黑战士】','【敌-黑暗弩手】','【敌-暗夜骑士】','【敌-嗜血刀客】','【敌-首席刺客】','【敌-陷阱之王】']
    player_info={}
    enemy_info={}
    #上面的变量是下面的函数都能使用

    def __init__(self):
        self.player=random.sample(self.player_list,3)#玩家和敌人的列表
        self.enemy=random.sample(self.enemy_list,3)
        self.show_role()
        self.order()
        self.pk_process()

    def GF(self):#随机生成属性
        X=random.randint(100,500)    
        G=random.randint(50,80)
        return X,G#输入两个元素成为元组要return

    def show_role(self):#字典记录名字，血，攻击信息
        for i in range(3):
            self.player_info[self.player[i]]=self.GF()#往字典插入键值——'字典名[键]=值!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1函数名的格式： self.GF() 
            self.enemy_info[self.enemy[i]]=self.GF()#将血，攻与名字对应上
        print('----------------- 角色信息 -----------------')
        print('你的人物：')
        for i in range(3):
            print('你的角色 {} \n血量：{}  \n攻击:{} '.format(self.player[i],self.player_info[self.player[i]][0],self.player_info[self.player[i]][1]))
            time.sleep(1.5)
        print('--------------------------------------------')
        print('电脑敌人：')
        for i in range(3):
            print('电脑 {} \n血量：{}  \n攻击:{} '.format(self.enemy[i],self.enemy_info[self.enemy[i]][0],self.enemy_info[self.enemy[i]][1]))        
            time.sleep(1.5)
        print('--------------------------------------------')
        input('请按回车继续。 \n')

    def order(self):#用字典将出场数字和名字对应上
        self.player_dic1={}
        for i in range(3):
            self.order = int(input('你要把'+self.player[i]+'放在第几位？（请输入数字1,2,3)'))
            self.player_dic1[self.order]=self.player[i]#用字典将出场数字和名字对应上
        print(self.player_dic1)
        self.player=[]
        #用字典键重新添加
        for i in range(1,4):
            self.player.append(self.player_dic1[i])#用新列表按顺序加名字,对应键值 1，2，3
        print(self.player)
        print(self.player_info)
    #print(self.player)#外部函数不能用内部的函数的变量

    def pk_process(self):
        self.round=1
        self.score=0
        for i in range(3):
            #先定义几个变量
            
            self.player_name=self.player[i]
            self.robot_name=self.enemy[i]
            self.player_life=self.player_info[self.player[i]][0]#将名字和血，攻击链接上
            self.player_attack=self.player_info[self.player[i]][1]
            self.robot_life=self.enemy_info[self.enemy[i]][0]
            self.robot_attack=self.enemy_info[self.enemy[i]][1]
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
        #print('{}\n血量:{}\n攻击：{}'.format(self.name,self.blood,self.attack))

class Assassin(role):
    def __init__(self):
        self.name='杀手'
        self.attack=random.randint(50,80)*5
        self.blood=random.randint(200,400)*3
        #print('{}\n血量:{}\n攻击：{}'.format(self.name,self.blood,self.attack))

class Bowman(role):
    def __init__(self):
        self.name='射手'
        self.attack=random.randint(50,80)*4
        self.blood=random.randint(200,400)*4
        #print('{}\n血量:{}\n攻击：{}'.format(self.name,self.blood,self.attack))

a=role()
b=Knight()
c=Assassin()
d=Bowman()

list1=[a,b,c,d]
for i in list1:
    print(i.name +'的血量是' +str(i.blood)+'攻击是'+str(i.attack))
#game=Game()
#knight=Knight()#继承后，实例化的函数不加父类名字 #Assassin=Assassin(role)错的
#Assassin=Assassin()
#Bowman=Bowman()
