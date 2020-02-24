def large_factor(n):
    a=1
    list1=[]
    while a<n:
        if n%a==0:
            list1.append(a)
        else:
            pass
        a+=1
    if list1==0:
        return 1
    else:
        return max(list1)

print(large_factor(15))