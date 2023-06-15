
#Combinational Problem

def uniquePaths(m, n):
    N=n+m-2
    r=m-1 #n-1
    res=1
    for i in range(1,r+1):
        res=res*(N-r+i)//i
    return int(res)

if __name__=="__main__":
    n=3
    m=2
    print(uniquePaths(m,n))