class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0, len(nums) -1 

        while l < r:
            midIndex = l + ((r-l) // 2)
            midNumber = nums[midIndex]

            if nums[r] < midNumber: # min is on the right
                l = midIndex + 1
            
            elif nums[r] > midNumber:  # min is on the left
                r = midIndex


        return nums[l]
