class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need={}
        win={}
        have=0
        required=len(set(t))

        l = 0
        minlen = float('inf')
        res = ""
        if len(s) < len(t):
            return ""
        for i in t:
            need[i]=need.get(i,0)+1
        for r in range(len(s)):
            c=s[r]
            win[c] = win.get(c, 0) + 1
            if c in need and win[c] == need[c]:
                have += 1
            while have == required:
                winl=r - l + 1
                if winl < minlen:
                    minlen = winl
                    res = s[l:r+1]

                left = s[l]

                if left in need and win[left] == need[left]:
                    have -= 1

                win[left] -= 1
                l += 1
        return res

