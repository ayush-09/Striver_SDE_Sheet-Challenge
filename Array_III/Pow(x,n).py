def myPow(x, n):
    ans=1
    num = n
    if n<0:
        num=-1*num
    while num>0:
        if num%2==0:
            x=x*x
            num=num/2
        else:
            ans=ans*x
            num=num-1
    if n<0:
        return 1/ans
    return ans

if __name__=="__main__":
    print(myPow(2.0000,10))