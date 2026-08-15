class Solution:
    def isPalindrome(self, s: str) -> bool:
        val=""
        for i in s:
            if i.isalnum():
                val += i.lower()
        new = val[::-1]
        return val==new
            

        