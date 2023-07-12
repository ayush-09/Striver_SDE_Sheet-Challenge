from collections import *

def twoSum(nums, target):
    h={}
    for i,num in enumerate(nums):
        r=target-num
        if r not in h:
            h[num]=i
        else:
            return [h[r],i]

# Coding Ninja
def pairSum(arr, s):
    # Write your code here.
    h=defaultdict(int)
    a=[]
    for i in arr:
        c=h[s-i]
        p=[i,s-i]
        while c>0:
            a.append(sorted(p))
            c-=1
        h[i]+=1

    return sorted(a)

if __name__=="__main__":
    print(twoSum(nums = [2,7,11,15], target = 9))
    print(pairSum([2,7,11,15],9))