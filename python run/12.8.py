class 成绩单():
    @classmethod
    def 录入成绩单(cls):
        cls.学生姓名 = input('请输入学生姓名：')
        cls.语文_成绩 = int(input('请输入语文考试成绩：'))
        cls.数学_成绩 = int(input('请输入数学考试成绩：'))
        cls.平均分=((cls.语文_成绩)+(cls.数学_成绩))/2

    @classmethod
    def 计算是否及格(cls):
        if cls.平均分 >= 60:
            return '及格'
        else:
            return '不及格'

    @classmethod
    def 考试结果(cls):
        grade=cls.计算是否及格()#参数传递
        
        print(grade)
        print(cls.学生姓名 + '的成绩单如下：')
        print('语文成绩：'+ str(cls.语文_成绩))
        print('数学成绩：{}'.format(cls.数学_成绩))
        print(cls.学生姓名 + '的评级是：{}'.format(grade))
    
成绩单.录入成绩单()
成绩单.考试结果()