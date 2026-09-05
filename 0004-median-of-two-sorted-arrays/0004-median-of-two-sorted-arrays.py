class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3=[]
        nums3= list(heapq.merge(nums1, nums2))
        n= len(nums3)
        if n%2!=0:
            mid = n//2
            return nums3[mid]

        else:
            l=nums3[(n//2)-1]
            r=nums3[n//2]
            return (l+r)/2


        