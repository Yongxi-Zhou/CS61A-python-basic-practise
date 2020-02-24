#不用修改代码，直接运行即可，尝试多输入几次非数字
while True:
    try:
        age = int(input('你今年几岁了？'))
        break#只有输入数字才可以break
    except ValueError:
        print('你输入的不是数字！')
if age < 18:
    print('不可以喝酒噢')