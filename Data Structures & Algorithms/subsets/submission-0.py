class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[[]]
        for num in nums:
            for s in res[:]:
                res.append(s+[num])
        return res