class Solution:
    def checkDivisibility(self, n: int) -> bool:
        num=n
        s=0
        p=1
        while num!=0:
            digit= num%10
            s += digit
            p *= digit
            num //= 10

        r= s+p
        return n%r==0


        