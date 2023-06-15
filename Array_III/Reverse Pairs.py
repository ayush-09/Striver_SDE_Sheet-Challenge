def merge(arr, l, m, r):
    t=[]
    left=l
    right=m+1
 
    while left<=m and right <=r:
        if arr[left] <= arr[right]:
            t.append(arr[left])
            left += 1
        else:
            t.append(arr[right])
            right += 1
    
    while left <=m:
        t.append(arr[left])
        left += 1
 
    
    while right <=r:
        t.append(arr[right])
        right += 1

    for i in range(l,r+1):
        arr[i]=t[i-l]

 
def countPair(arr,low,mid,high):
    right=mid+1
    cnt=0
    for i in range(low,mid+1):
        while right<=high and arr[i]>2*arr[right]:
            right+=1
        cnt+=(right-(mid+1))
    return cnt

def mergeSort(arr, low, high):
    cnt = 0
    if low >= high:
        return cnt
    mid = low + (high-low) // 2
    cnt+=mergeSort(arr, low, mid)    # left half
    cnt+=mergeSort(arr, mid + 1, high)  # right half
    cnt+=countPair(arr,low,mid,high) #add this function 
    merge(arr, low, mid, high)  # merging sorted halves
    return cnt

def reversePair(nums):
    n=len(nums)
    return mergeSort(nums,0,n-1)
    
if __name__=="__main__":
    nums=[4, 1, 2, 3, 1]
    print(reversePair(nums))