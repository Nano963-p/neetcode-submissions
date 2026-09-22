class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) -1
        l_max= 0
        r_max=0
        water = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] > l_max:
                    l_max = height[left]
                else:
                    water = water + l_max - height[left]
                left = left + 1
            else:
                if height[right] > r_max:
                    r_max = height[right]
                else:
                    water = water + r_max - height[right]
                right = right - 1

        return water
