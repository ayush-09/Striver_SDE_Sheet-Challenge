def fourSum(nums,target):
    s=set()
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            hs=set()
            for k in range(j+1,len(nums)):
                fsum=nums[i]+nums[j]
                fsum+=nums[k]
                forth=target-fsum
                if forth in hs:
                    temp=[nums[i],nums[j],nums[k],forth]
                    temp.sort()
                    s.add(tuple(temp))
                hs.add(nums[k])
    return s

if __name__=="__main__":
    print(fourSum([1,0,-1,0,-2,2],0))