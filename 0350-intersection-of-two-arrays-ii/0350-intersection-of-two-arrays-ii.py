class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s1=sorted(nums1)
        s2=sorted(nums2)
        i=0
        j=0
        res=[]
        while i<len(s1) and j<len(s2):
            if s1[i] < s2[j]:
                i+=1
            elif s2[j]<s1[i]:
                j+=1
            else:
                res.append(s1[i])
                i+=1
                j+=1
        return res
        