class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        op=set()
        hor=set()

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    diff=target-(nums[i]+nums[j]+nums[k])

                    if diff in hor:
                        lis=[diff,nums[i], nums[j], nums[k]]
                        lis.sort()
                        tupl=tuple(lis)
                        op.add(tupl)
            hor.add(nums[i])
        return [list(o) for o in op]