def merge(nums1, m, nums2, n):
        nums1[m:] = nums2[:n]
        nums1.sort()
        return nums1

if __name__== "__main__":
        nums1=[1,2,3,0,0,0]
        m=3
        nums2=[2,5,6]
        n=3
        print(merge(nums1=nums1,m=m,nums2=nums2,n=n))