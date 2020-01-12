movies = {
'妖猫传':['黄轩','染谷将太'],
'无问西东':['章子怡','王力宏','祖峰'],
'超时空同居':['雷佳音','佟丽娅'],
}

actor=input('你找的演员？')
for i in movies:
    allactor=movies[i]
    if actor in allactor:
        print(actor+'出演了电影'+i)
        #in 表示包含
        #for i in 字典，出来的值是key value