
def merge(arr, l, m, r):
    t=[]
    left=l
    right=m+1

    cnt=0  #1
 
    while left<=m and right <=r:
        if arr[left] <= arr[right]:
            t.append(arr[left])
            left += 1
        else:
            t.append(arr[right])
            cnt+=m-left+1  #2
            right += 1
    
    while left <=m:
        t.append(arr[left])
        left += 1
 
    
    while right <=r:
        t.append(arr[right])
        right += 1

    return cnt  #3
 

def mergeSort(arr, low, high):
    cnt = 0
    if low >= high:
        return cnt
    mid = low + (high-low) // 2
    cnt += mergeSort(arr, low, mid)    # left half
    cnt += mergeSort(arr, mid + 1, high)  # right half
    cnt += merge(arr, low, mid, high)  # merging sorted halves
    return cnt

def noOfinversion(arr,n):
    #merge sort for optimize
    return mergeSort(arr,0,n-1)
    
if __name__ == "__main__":
    a = [5, 4, 3, 2, 1]
    n = 5
    cnt = noOfinversion(a, n)
    print(cnt)


