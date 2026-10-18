class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        lastseen={}
        for i,n in enumerate(nums):
            if n in lastseen and i-lastseen[n]<=k:
                return True
            lastseen[n]=i
        return False
                

            
            

        