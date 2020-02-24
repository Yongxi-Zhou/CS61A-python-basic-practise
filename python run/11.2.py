while True:
    try:
        x=input('除数')
        y=input('被除数')
        z=x/y
        print('商是{}'.format(x/y))
        break
    except ZeroDivisionError:
        print('0不能做除数')
    except TypeError:
        print('数据类型错了')