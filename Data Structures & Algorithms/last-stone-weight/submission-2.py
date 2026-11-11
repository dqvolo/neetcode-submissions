import heapq as hp
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones=[-x for x in stones]
        hp.heapify(stones)
        while len(stones) > 1:
            x = -hp.heappop(stones)
            y = -hp.heappop(stones)

            a = x - y

            if a != 0:
                hp.heappush(stones, -a)
        return -stones[0] if stones else 0