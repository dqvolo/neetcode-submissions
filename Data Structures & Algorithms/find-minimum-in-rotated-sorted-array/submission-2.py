class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        lmin=nums[l]
        rmin=nums[r]
        res=rmin
        while l<r:
            if lmin<rmin:
                l+=1
                lmin=min(lmin,nums[l])
                res=lmin
            else:
                r-=1
                rmin=min(rmin, nums[r])
                res=rmin
        return res