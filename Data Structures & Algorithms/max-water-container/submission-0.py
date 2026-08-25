class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_area = (right - left) * min(heights[right],heights[left])

        while left < right:
            if min(heights[right],heights[left]) ==heights[right] :
                right -=1
            else:
                left +=1

            res = (right - left) * min(heights[right],heights[left])
            if res > max_area:
                max_area = res
        return max_area
        

