class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums)==0:
            return [[]]
        perms=self.permuteUnique(nums[1:])
        res=set()
        for p in perms:
            for i in range(len(nums)):
                p_copy=p.copy()
                p_copy.insert(i,nums[0])
                res.add(tuple(p_copy))
        return [list(p) for p in res]
        