class 乘法表():
    def __init__(self,i):#只要有实例执行就会调用init函数
        self.i=i#利用初始函数创建属性

    def 打印(self):
        print('''-----代码中运行了这些方法【1】------
三三乘法表 = 乘法表({})
三三乘法表.打印()

---------代码运行的效果【1】--------'''.format(self.i))
        for i in range(1,1+self.i):
            for x in range(1,i+1):
                print( '%d X %d = %d' % (i ,x ,i*x) ,end = '  ' )
            print('  ')

三三乘法表 = 乘法表(3)#只要实例化了，自动执行init，类属性直接传递到init函数中
三三乘法表.打印()

五五乘法表 = 乘法表(5)
五五乘法表.打印()