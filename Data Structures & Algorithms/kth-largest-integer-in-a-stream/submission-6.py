import heapq as hp

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums

        hp.heapify(self.nums)

        while len(self.nums) > self.k:
            hp.heappop(self.nums)
    def add(self, val: int) -> int:
        hp.heappush(self.nums, val)

        if len(self.nums)>self.k:
            hp.heappop(self.nums)
        return self.nums[0]