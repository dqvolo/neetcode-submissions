class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ans=[]
        for num in nums:
            if val!=num:
                ans.append(num)
        nums[:]=ans
        k=int(len(nums))
        return k
