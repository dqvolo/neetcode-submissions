import heapq as hp
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda t: t[1])

        curcap=0
        minheap=[] #[end,num]

        for i in trips:
            num, start, end=i
            while minheap and minheap[0][0]<=start:
                curcap-=minheap[0][1]

                hp.heappop(minheap)
            curcap+=num
            if curcap>capacity:
                return False
            hp.heappush(minheap, [end, num])
        return True
