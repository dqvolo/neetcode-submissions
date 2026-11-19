class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        res=[]
        sol=[]

        def bt():
            if len(sol)==n:
                res.append(sol.copy())
                return
            for num in nums:
                if num not in sol:
                    sol.append(num)
                    bt()
                    sol.pop()
        bt()
        return res