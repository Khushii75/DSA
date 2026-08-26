class Solution:
    def reinitializePermutation(self, n: int) -> int:
        res, i=0,1
        while res ==0 or i>1:
            if i<n/2:
                i *= 2
            else:
                i= (i-n/2)*2+1
            res += 1
        return res
        