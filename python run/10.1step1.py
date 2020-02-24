#项目1的部分代码
import time,random
player_list =  ['【狂血战士】','【森林箭手】','【光明骑士】','【独行剑客】','【格斗大师】','【枪弹专家】']
enemy_list = ['【暗黑战士】','【黑暗弩手】','【骷髅骑士】','【嗜血刀客】','【首席刺客】','【陷阱之王】']
player=random.sample(player_list,3)
enemy=random.sample(enemy_list,3)
print(player)
print(enemy)
#展示角色，封装1
def show_role(player_life,player_attack,enemy_life,enemy_attack):
    print('{} \n血量:{}  \n攻击:{}'.format(random.choice(player),player_life,player_attack))
    print('{} \n血量:{}  \n攻击:{}'.format(random.choice(enemy),enemy_life,enemy_attack))
    print('------------------------')

#双方PK，封装2
def process(player_life,player_attack,enemy_life,enemy_attack):#定义多个变量
    while player_life > 0 and enemy_life > 0:
            player_life = player_life - enemy_attack 
            enemy_life = enemy_life - player_attack
            print('你发起了攻击，【敌人】剩余血量%s'%(enemy_life))
            print('敌人向你发起了攻击，【玩家】的血量剩余%s'%(player_life))
            print('-----------------------')
            time.sleep(1.2)
    end(player_life,enemy_life)#pk结束后执行end函数判断
#打印战果
def end(player_life,enemy_life):
    if player_life > 0 and enemy_life <= 0:
        print('敌人死翘翘了，这局你赢了')
    elif player_life <= 0 and enemy_life > 0:
        print('悲催，这局敌人把你干掉了！')
    else:
        print('哎呀，这局你和敌人同归于尽了！')
    print('-----------------------')

def main(player_life,player_attack,enemy_life,enemy_attack):
    show_role(player_life,player_attack,enemy_life,enemy_attack)
    process(player_life,player_attack,enemy_life,enemy_attack)
main(random.randint(100,500),random.randint(50,80),random.randint(100,300),random.randint(60,90))