class Solution:
    def isValid(self, s: str) -> bool:
        a=[]
        for i in s:
            if i=='(' or i == '{' or i=='[':
                a.append(i)
            else:
                if len(a)==0:
                    return False
                elif i==')' and a[-1]=='(':
                    a.pop()
                elif i =='}' and a[-1]== '{':
                    a.pop()
                elif i==']' and a[-1]=='[':
                    a.pop()
                else:
                    return False

        return len(a)==0

        