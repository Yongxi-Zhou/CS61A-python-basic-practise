class system():
    list=[]
    name=''
    kpi=0

    @classmethod
    def input_info(cls):
        cls.name=input('名字是？')
        cls.kpi=int(input('kpi多少？'))
        cls.list=['bob','candy','jony',' kelly']

    @classmethod
    def check_name(cls):
        if cls.name in cls.list:
            print('录入正确')
        else:
            print('录入错误！{}不是本公司员工'.format(cls.name))
        
    @classmethod
    def print_record(cls):
        if cls.kpi>95:
            print('明星')
        elif 80<= cls.kpi<95:
            print('优秀')
        else:
            print('一般')
system.input_info()
system.check_name()
system.print_record()