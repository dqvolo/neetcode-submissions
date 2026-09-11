class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l=max(weights)
        r=sum(weights)
        res=r
        def can(m):
            ships, capacity=1,m
            for w in weights:
                if capacity-w<0:
                    ships+=1
                    capacity=m
                capacity-=w
            return ships<=days

        while l<=r:
            m=(l+r)//2
            if can(m):
                res=min(res, m)
                r=m-1
            else:
                l=m+1 
        return res