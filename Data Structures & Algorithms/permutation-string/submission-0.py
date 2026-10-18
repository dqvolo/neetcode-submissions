class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l=0
        r=len(s1)-1
        window = s2[l:r+1]
        while r<=len(s2):
            window = s2[l:r+1]
            
            if sorted(s1)==sorted(window):
                return True
            else:
                r+=1
                l+=1
        return False