class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ls = sorted(nums)
        rs =[]

        for i in range(len(nums)):
            if i > 0 and ls[i] == ls[i-1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while (left < right):
                sum = ls[i] + ls[left] + ls[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -=1

                elif sum == 0 and i!=left and left !=right:
                    rs.append([ls[i] , ls[left] , ls[right]])
                    left += 1
                    right -=1
                    while left < right and ls[left] == ls[left-1]:
                        left+=1
                    while left < right and ls[right] == ls[right+1]:
                        right-=1

        return rs

