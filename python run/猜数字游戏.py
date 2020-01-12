import random
n=random.randint(1,10)
i=1
while i:
    n1=int(input('猜猜数字？'))
    if n1>n:
        print('你猜大了')
    if n1<n:
        print('你猜小了')
    if n1==n:
        print('你猜对了！')
        break