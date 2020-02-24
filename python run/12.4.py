class 类():

    @classmethod
    def 打印类属性(cls):
        print('好的，我把它存了起来，然后翻了888倍还给你：{}'.format((cls.变量)*88))
类.变量 = int(input('你的幸运数是多少？请输入一个整数。'))#在外部通过赋值修改内部变量  类.变量名=XXX
类.打印类属性()

class 类():
    @classmethod
    def 增加类属性(cls):
        cls.变量 = input('请随意输入字符串：')#在函数内部加变量
类.增加类属性()
print('打印新增的类属性：')
print(类.变量)