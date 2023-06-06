def nextPermutation(permutation, n):
    # Write your code here.
    # Return a list.
    if n<2:
        return permutation
    l=len(permutation)-2
    while l>=0 and permutation[l]>=permutation[l+1]:
        l-=1
    if l<0:
        return reversed(permutation)
    r=l+1
    while r<len(permutation) and permutation[r]>permutation[l]:
        r+=1
    r-=1
    if r<n:
        permutation[l],permutation[r]=permutation[r],permutation[l]
    permutation[l+1:]=reversed(permutation[l+1:])

    return permutation