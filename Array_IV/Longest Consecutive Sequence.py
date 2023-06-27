def longestConsecutive(nums):
    h=set()
    for i in nums:
        h.add(i)
    l=0
    for i in h:
        if i-1 not in h:
            cur=i
            c=1
            while cur+1 in h:
                cur+=1
                c+=1
            l=max(l,c)
    return l

if __name__=="__main__":
    print(longestConsecutive([100,4,200,1,3,2]))