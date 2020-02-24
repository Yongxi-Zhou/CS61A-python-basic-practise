def hailstone(n):
    length=1
    while n!=1:
        if n%2==0:
            n=n//2
        else:
            n=(n*3)+1
        print(n)
        length+=1
    return length

print(hailstone(10))