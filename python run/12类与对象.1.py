class 类A():
    变量1 = 100
    变量2 = 200
    @classmethod #声名变量可以用在类方法中，要用到类中的变量才要写
    def 函数1(cls):#函数调用类属性
        print(cls.变量1)#调用属性格式： cls.属性
        print(cls.变量2)
类A.函数1()

class 智能机器人():
    胸围 = 33
    腰围 = 44
    臀围 = 55
    def 打招呼():
        print('主人你好！')
    def 卖萌():
        print('主人，求抱抱！')

    @classmethod
    def 自爆三维(cls):
        print(智能机器人.胸围)
        print(cls.腰围)#调用属性格式： cls.属性
        print(cls.臀围)
智能机器人.自爆三维()#打印时括号不用加cls