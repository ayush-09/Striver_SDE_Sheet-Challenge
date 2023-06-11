from collections import Counter\

def majorityElement(nums):
    a=Counter(nums)
    for i,j in a.items():
        if j>(len(nums)/2):
            return i
    return -1

print(majorityElement([3,2,3]))