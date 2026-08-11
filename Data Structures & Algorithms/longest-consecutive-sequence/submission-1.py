class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        long = 0
        for num in nums:
            if (num - 1) not in numbers:
                count = 0
                while(num in numbers):
                    count +=1
                    num +=1
                long = max(long,count)

        return long