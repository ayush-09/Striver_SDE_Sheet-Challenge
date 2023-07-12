def subarraysXor(arr, x):
    n = len(arr)  # size of the given array.
    cnt = 0

    # Step 1: Generating subarrays:
    for i in range(n):
        xorr = 0
        for j in range(i, n):

            # step 2: calculate XOR of all elements:
            xorr = xorr ^ arr[j]

            # step 3: check XOR and count:
            if (xorr == x):
                cnt += 1

    return cnt

if __name__=="__main__":
    print(subarraysXor([5,3,8,3,10],8))