class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        
        freq = [0]*26
        l=0
        res=0
        for r in range(len(s)):
            freq[ord(s[r])- ord('a')] += 1

            while freq[ord(s[r])- ord('a')] > 2:
                freq[ord(s[l])- ord('a')] -= 1
                l +=1
            res= max(res, r-l+1)
        return res



        