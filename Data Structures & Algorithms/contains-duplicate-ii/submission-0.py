class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen={}
        x=0
        for i in range(len(nums)):
            if nums[i] in seen:
                x=seen[nums[i]]
                if i-x<=k:
                    return True
            seen[nums[i]]=i
        return False
        