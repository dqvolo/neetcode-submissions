class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq as hp
        dis=[]

        for x,y in points:
            d=x*x+y*y
            dis.append((d,[x,y]))

        hp.heapify(dis)

        res=[]

        i=0
        while i<k:
            res.append(hp.heappop(dis)[1])
            i+=1
        return res