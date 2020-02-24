class 基础机器人():
    def __init__(self,参数):
        self.姓名 = 参数

    def 自报姓名(self):
        print('我是' + self.姓名 + '！')     

    def 卖萌(self):
        print('主人，求抱抱！')

class 高级机器人(基础机器人):
    def __init__(self,参数,IQ):
        self.姓名=参数
        self.IQ=IQ
    
    def 自报姓名(self):
        print('我是高级机器人{}，我的智商{}'.format(self.姓名,self.IQ))       

    def 卖萌(self):
        print('主人，每次想到怎么欺负你的时候，就感觉自己全身biubiubiu散发着智慧的光芒！')

安迪 = 高级机器人('安迪',150)#实例化参数自动代入到init
安迪.自报姓名()
安迪.卖萌()