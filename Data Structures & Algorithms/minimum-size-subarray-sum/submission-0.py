class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        win=0
        minwin = float('inf')
        for r in range(len(nums)):
            win+=nums[r]

            while win>=target:
                minwin=min(minwin, r-l+1)
                win-=nums[l]
                l+=1
        return 0 if minwin==float('inf') else minwin