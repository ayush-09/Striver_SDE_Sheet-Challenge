def maxSubarraySum(arr, n) :
    maxi=arr[0]
    s=0
    for i in range(n):
        s+=arr[i]
        maxi=max(maxi,s)
        if s<0:
            s=0
    if maxi<0:
        return 0
    else:
        return maxi

print(maxSubarraySum([18,-6,-6,-5,7,10,16,-6,-2,0],7))