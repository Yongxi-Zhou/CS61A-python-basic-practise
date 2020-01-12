import time
import random

player_life=random.randint(100,500)
sb_life=random.randint(100,200)
player_attack=random.randint(50,70)
sb_attack=random.randint(70,80)

print('【玩家】\n血量：'+str(player_life)+ '\n攻击：'+str(player_attack))  # 自定义玩家角色的血量和攻击，用换行符'\n'来优化视觉
print('------------------------')  # 辅助功能，起到视觉分割的作用，让代码的运行结果更清晰
time.sleep(1.5)

print('【敌人】\n血量：'+str(sb_life)+'\n 攻击：'+str(sb_attack))
print('------------------------')
time.sleep(1.5)

while sb_life>0 and player_life>0:
    sb_life=sb_life-player_attack
    print('你发起了攻击，【敌人】剩余血量'+str(sb_life))
    time.sleep(1.5)
    print('------------------------')

    player_life=player_life-sb_attack
    print('敌人向你发起了攻击，【玩家】剩余血量'+str(player_life))
    time.sleep(1.5)
    print('------------------------')
    
if sb_life<=0<player_life:
    print('敌人死翘翘了，你赢了！')
elif player_life<=0<sb_life:
    print('敌人赢了，你死翘翘了！')
else:
    print('同归于尽')
#把if放外面是跳出循环再判断，这是肯定有一个小于0

