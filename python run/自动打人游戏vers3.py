import time
import random

score_sb=0
score_player=0

for i in range(3):
    print('现在是第'+str(i+1)+'局')
    player_life=random.randint(100,200)
    sb_life=random.randint(100,200)
    player_attack=random.randint(50,70)
    sb_attack=random.randint(50,70)

    print('【玩家】\n血量：'+str(player_life)+ '\n攻击：'+str(player_attack))  # 自定义玩家角色的血量和攻击，用换行符'\n'来优化视觉
    print('------------------------')  # 辅助功能，起到视觉分割的作用，让代码的运行结果更清晰
    time.sleep(1.5)

    print('【敌人】\n血量：'+str(sb_life)+'\n 攻击：'+str(sb_attack))
    print('------------------------')
    time.sleep(1.5)

    while sb_life>0 and player_life>0:
        sb_life=sb_life-player_attack
        player_life=player_life-sb_attack
        print('你发起了攻击，【敌人】剩余血量'+str(sb_life))
        print('敌人向你发起了攻击，【玩家】剩余血量'+str(player_life))
        time.sleep(1.5)
        if sb_life<=0<player_life:
            score_player=score_player+1
        elif sb_life<=0<player_life:
            score_sb += 1
        else:
            print('同归于尽')
        print('现在玩家和sb的比分是'+str(score_player)+'：'+str(score_sb))
        print('------------------------')
        #缩进代表在while的循环体中

if score_sb<score_player:
    print('玩家赢了')
else:
    print('sb赢了')