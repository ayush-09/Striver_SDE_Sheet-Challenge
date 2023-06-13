
def twoSum(nums, target):
    h={}
    for i,num in enumerate(nums):
        r=target-num
        if r not in h:
            h[num]=i
        else:
            return [h[r],i]

if __name__=="__main__":
    print(twoSum(nums = [2,7,11,15], target = 9))