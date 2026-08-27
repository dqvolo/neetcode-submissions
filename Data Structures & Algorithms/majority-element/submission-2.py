class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        a=len(nums)
        return nums[a//2]