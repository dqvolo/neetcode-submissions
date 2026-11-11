class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq as hp
        nums=[-x for x in nums]
        hp.heapify(nums)

        i=0
        while i<k-1:
            hp.heappop(nums)
            i+=1
        return -nums[0]