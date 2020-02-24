class 出租车():
    def __init__(self,参数1,参数2,参数3):
        self.每公里费用 = 参数1
        self.最低公里 = 参数2
        self.最低费用 = 参数3

    def 计费(self):
        self.记录行程()
        self.统计费用()
        self.结算信息()
        
    def 记录行程(self):
        self.route=float(input('走了多少公里？'))

    def 统计费用(self):
        if self.route<=self.最低公里:
            self.cost=self.最低费用#所有变量全部都要加self.!!!!!!!!
        else:
            self.cost=self.最低费用+self.每公里费用*(self.route-self.最低公里)
    
    def 结算信息(self):
        print('花费了{}元'.format(self.cost))

class 电动(出租车):
    def 结算信息(self):
        print('花费了{}元'.format((self.cost)*0.8))

小王的出租车 = 出租车(2.5,3,15)
小王的出租车.计费()

小王的电车 = 电动(2.5,3,15)
小王的电车.计费()