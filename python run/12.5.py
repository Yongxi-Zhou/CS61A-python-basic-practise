import time
class 念诗类():
    一首诗 = ['《卜算子》','我住长江头，','君住长江尾。','日日思君不见君，','共饮长江水。']
    
    @classmethod
    def 念诗函数(cls):
        cls.who=input('请输入你想给谁念诗：')#内部加入变量
        print('念给'+ str(cls.who) +'的诗：')
        for i in cls.一首诗:
            print(i)
            time.sleep(1)

念诗类.念诗函数()