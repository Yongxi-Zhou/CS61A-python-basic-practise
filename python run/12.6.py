class 成绩单():
    @classmethod
    def 录入成绩单(cls):
        cls.学生姓名 = input('请输入学生姓名：')
        cls.语文_成绩 = int(input('请输入语文成绩：'))
        cls.数学_成绩 = int(input('请输入数学成绩：'))
        cls.平均分= int(((cls.语文_成绩)+(cls.数学_成绩))/2)
    @classmethod
    def 打印成绩单(cls):
        print(cls.学生姓名 + '的成绩单如下：')
        print('语文成绩：'+ str(cls.语文_成绩))
        print('数学成绩：{}'.format(cls.数学_成绩))
    @classmethod
    def 打印平均分(cls):
        print('{}平均分：{}'.format(cls.学生姓名,cls.平均分))

    @classmethod
    def 评级(cls):#内部变量要加cls
        if cls.平均分>=90:
            print('{}的评级是优秀'.format(cls.学生姓名))
        elif 80<=cls.平均分<90:
            print('{}的评级是良好'.format(cls.学生姓名))
        elif 60<=cls.平均分<80:
            print(('{}的评级是中'.format(cls.学生姓名)))
        else:
            print(('{}的评级是差到嗨那样'.format(cls.学生姓名)))
    
成绩单.录入成绩单()
成绩单.打印成绩单()
成绩单.打印平均分()
成绩单.评级()