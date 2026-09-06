class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        list1=[]
        list2=[]
        k=k%len(nums)
        l,r=len(nums)-k,len(nums)-1

        while l<=r:
            list1.append(nums[l])
            l+=1
    
        L,R=0,len(nums)-k-1
        while L<=R:
            list2.append(nums[L])
            L+=1
        nums[:]=list1+list2
        

        