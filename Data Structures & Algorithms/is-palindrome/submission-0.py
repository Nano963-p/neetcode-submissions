class Solution:
    def isPalindrome(self, s: str) -> bool:
        l1 = []
        l2 = []
        l = len(s)
        for i in range(l):
            c = s[i].lower()
            if c.isalnum():
                l1.append(c)
            a = s[l - i - 1].lower()
            if a.isalnum():
                l2.append(a)
            
        if l1 == l2:
            return True
        return False
