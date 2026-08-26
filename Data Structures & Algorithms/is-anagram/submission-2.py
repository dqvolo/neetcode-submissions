class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen1={}
        seen2={}
        for i in range(len(s)):
            if s[i] not in seen1:
                seen1[s[i]]=1
            else:
                seen1[s[i]]+=1
        for i in range(len(t)):
            if t[i] not in seen2:
                seen2[t[i]]=1
            else:
                seen2[t[i]]+=1
        if seen1==seen2:
            return True
        return False
