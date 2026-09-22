class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        for i , e in enumerate(heights):
            while stack and e < heights[stack[-1]]:
                a = stack.pop()
                if not stack :
                    width = i
                else :
                    width = i - stack[-1] - 1
                area = width * heights[a]
                if max_area < area :
                    max_area = area
            stack.append(i)
        n = len(heights)
        while stack:
            a = stack.pop()
            if not stack:
                width = n 
            else :
                width = n - stack[-1] - 1
            area = width * heights[a]
            if max_area < area :
                max_area = area
        return max_area    
