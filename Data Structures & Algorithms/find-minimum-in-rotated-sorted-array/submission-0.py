class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0, len(nums) -1 

        while l <= r:
            midIndex = l + ((r-l) // 2)
            midNumber = nums[midIndex]

            if nums[l] < midNumber: # min is on the left
                r = midIndex - 1
            else: # min is on the right
                l = midIndex + 1


        return min(nums)
