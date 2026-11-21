class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]
        def bt(i,c):
            if len(c)==k:
                res.append(c.copy())
            for j in range(i,n+1):
                c.append(j)
                bt(j+1,c)
                c.pop()
        bt(1,[])
        return res