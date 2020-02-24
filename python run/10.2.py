import random,time
player_list =  ['【狂血战士】','【森林箭手】','【光明骑士】','【独行剑客】','【格斗大师】','【枪弹专家】']
enemy_list = ['【敌-暗黑战士】','【敌-黑暗弩手】','【敌-暗夜骑士】','【敌-嗜血刀客】','【敌-首席刺客】','【敌-陷阱之王】']
player=random.sample(player_list,3)#玩家和敌人的列表
enemy=random.sample(enemy_list,3)
player_info={}
enemy_info={}
#上面的变量是下面的函数都能使用

def GF():#随机生成属性
    X=random.randint(100,500)    
    G=random.randint(50,80)
    return X,G#输入两个元素成为元组要return

def show_role():#字典记录名字，血，攻击信息
    for i in range(3):
        player_info[player[i]]=GF()#往字典插入键值——'字典名[键]=值
        enemy_info[enemy[i]]=GF()#将血，攻与名字对应上
    print('----------------- 角色信息 -----------------')
    print('你的人物：')
    for i in range(3):
        print('你的角色 {} \n血量：{}  \n攻击:{} '.format(player[i],player_info[player[i]][0],player_info[player[i]][1]))
        time.sleep(1.5)
    print('--------------------------------------------')
    print('电脑敌人：')
    for i in range(3):
        print('电脑 {} \n血量：{}  \n攻击:{} '.format(enemy[i],enemy_info[enemy[i]][0],enemy_info[enemy[i]][1]))        
        time.sleep(1.5)
    print('--------------------------------------------')
    input('请按回车继续。 \n')

def order():#用字典将出场数字和名字对应上
    global player#要把变量全局化
    player_dic1={}
    for i in range(3):
        order = int(input('你要把'+player[i]+'放在第几位？（请输入数字1,2,3)'))
        player_dic1[order]=player[i]#用字典将出场数字和名字对应上
    print(player_dic1)
    player=[]
    #用字典键重新添加
    for i in range(1,4):
        player.append(player_dic1[i])#用新列表按顺序加名字,对应键值 1，2，3
    print(player)

print(player_info)
print(player)#外部函数不能用内部的函数的变量

def pk_process():
    round=1
    score=0
    for i in range(3):
        #先定义几个变量
        global player#将line 39的变量全局化，这个变量之前也一定要是全局变量
        player_name=player[i]
        robot_name=enemy[i]
        player_life=player_info[player[i]][0]#将名字和血，攻击链接上
        player_attack=player_info[player[i]][1]
        robot_life=enemy_info[enemy[i]][0]
        robot_attack=enemy_info[enemy[i]][1]
        print('\n----------------- 【第{}局】 -----------------' .format(round))
        print('玩家角色：{} VS 敌方角色：{}'.format(player_name,robot_name))
        print('{}血量：{}  攻击：{}'.format(player_name,player_life,player_attack))
        print('{}血量：{}  攻击：{}'.format(robot_name,robot_life,robot_attack))
        time.sleep(2)

        while player_life>0 and robot_life>0:
            player_life=player_life-robot_attack
            robot_life=robot_life-player_attack
            print('{}发起攻击，{}剩余血量{}'.format(player_name,robot_name,robot_life))
            print('{}发起攻击，{}剩余血量{}'.format(robot_name,player_name,player_life))
            time.sleep(1.5)
        print(show_result(player_life,robot_life)[1])
        score+=show_result(player_life,robot_life)[0]
        print("第{}局player比分是{}".format(round,score))
        round+=1

    input=('点击回车查看结果')
    if score>=1:
        print('player win')
    elif score<0:
        print('robot win')
    else:
        print('Fair!')

def show_result(player_life,robot_life):#要定义才能传递参数给上面
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
def main():
    show_role()
    order()
    pk_process()
main()