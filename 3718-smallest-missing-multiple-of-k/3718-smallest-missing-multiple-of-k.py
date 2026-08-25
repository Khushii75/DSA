class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        mul=k
        while mul in nums:
            mul += k

        return mul
        