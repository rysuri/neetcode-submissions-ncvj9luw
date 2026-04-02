class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxWater = 0

        l = 0
        r = len(heights) -1 

        while l < r:
            area = (r - l) * min(heights[r],heights[l])

            if area > maxWater:
                maxWater = area
                
            if heights[r] > heights[l]:
                l +=1
            elif heights[r] < heights[l]:
                r -= 1  
            else:
                l += 1
                r -= 1
        return maxWater
            