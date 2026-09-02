class Solution:
    def validPalindrome(self, s: str) -> bool:
        l=0
        r=len(s)-1
        while l<r:
            if s[l]==s[r]:
                l+=1
                r-=1
            else:
                return self.validafterskip(s, l+1, r) or self.validafterskip(s, l, r-1)
        return True

    def validafterskip(self, s, l, r):
        while l<r:
            if s[l]==s[r]:
                l+=1
                r-=1
            else:
                return False
        return True