import time,random
list1=['石头','剪刀','布']
computer_choice=''
user_choice=""
computer_choice=random.choice(list1)
user_choice=input('剪刀石头布')
while user_choice not in list1:#not in list语法
    print('输入有误，请重新输入')
    user_choice=input("剪刀石头布")
#双方亮拳
print('电脑的是{}'.format(computer_choice))
print('我出的是{}'.format(user_choice))

#判断胜负
if computer_choice==user_choice:
    print('打平')
elif user_choice==list1[list1.index(computer_choice)-1]:
    print('player wins')
else:
    print('robot wins')
