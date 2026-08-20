class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        prev1=nums[0]
        prev2=0

        for i in range(1, len(nums)):
            take= nums[i]+prev2
            skip= prev1

            current= max(take, skip)
            prev2=prev1
            prev1=current
        return prev1
        