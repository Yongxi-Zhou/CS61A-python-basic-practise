class 出租车():
    def __init__(self,cost,front,front_mile):
        self.cost=cost
        self.front=front
        self.front_mile=front_mile

    def 计费(self):
        公里数 = float(input('请输入行程公里数：'))
        if 公里数>self.front_mile:
            费用 = (公里数-self.front_mile) * 2.5 + self.front
            print('费用一共是：' + str(费用) + '元')
        else:
            费用 = self.front
            print('费用一共是：' + str(费用) + '元')

小王的出租车 = 出租车(10,20,4)
小王的出租车.计费()

小李的出租车 = 出租车(10,12,2)
小李的出租车.计费()