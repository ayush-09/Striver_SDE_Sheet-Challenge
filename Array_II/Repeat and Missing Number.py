def missingAndRepeating(arr, n):
    # Write your code here
    s=set()
    a=sum(arr) #sum of arr
    rs= n*(n+1)//2 #sum of n numbers
    o=[]
    for i in arr:
        if i in s:
            o.append(i)
        s.add(i)

    #missing
    m=rs-a+o[0] # sum of n numbers - (sum of arr-repeating no)
    #print(m)
    return m,o[0]

if __name__=="__main__":
    print(missingAndRepeating([5,4,2,4,1],5))