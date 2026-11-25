class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res=[]
        maxr=-1
        for i in range(len(arr)-1,-1,-1):
            res.append(maxr)
            maxr=max(maxr,arr[i])
        return res[::-1]