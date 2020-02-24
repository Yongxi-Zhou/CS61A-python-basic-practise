class hahah():
    参数 = 10
    @classmethod
    def 加100函数(cls):
        总和 = cls.参数 + 100
        print('计算结果如下：')
        print(总和)

hahah.加100函数()

class hahah():
    def 加100函数():
        总和 = 参数 + 100
        print('计算结果如下：')
        print(总和)
参数 = 10#引用外部参数不用加 @classmethod

hahah.加100函数()