class poet():
    一首诗 = ['《卜算子》','我住长江头，','君住长江尾。','日日思君不见君，','共饮长江水。']
    @classmethod#引用内部参数要@classmethod
    def 念诗函数(cls):
        for i in cls.一首诗:
            print(i)

poet.念诗函数()

class poet():#引用外部参数
    def 念诗函数():
        for i in 一首诗:
            print(i)
一首诗 = ['《卜算子》','我住长江头，','君住长江尾。','日日思君不见君，','共饮长江水。']
poet.念诗函数()

class 念诗类():
    一首诗 = ['《卜算子》','我住长江头，','君住长江尾。','日日思君不见君，','共饮长江水。']
    
    @classmethod
    def 念诗函数(cls,title):
        print('写给{}的一封信'.format(title))
        for i in cls.一首诗:
            print(i)

念诗类.念诗函数('张三')#函数变量要写上外部参数