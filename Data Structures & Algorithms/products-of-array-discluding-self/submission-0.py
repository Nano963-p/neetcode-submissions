class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums)
        l = 1
        i = 0
        for i in range(len(nums)):
            res[i] = l
            l = nums[i]*l
        r = 1
        i = 0
        for i in range(len(nums)- 1,-1, -1):
            res[i]= res[i]  * r
            r = nums[i] * r
        return res


