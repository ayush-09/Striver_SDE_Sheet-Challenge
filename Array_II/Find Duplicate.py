def findDuplicate(nums):
    s=set()
    for i in nums:
        if i in s:
            return i
        s.add(i)
    return -1

if __name__=="__main__":
    nums=[1,3,4,2,2]
    print(findDuplicate(nums))