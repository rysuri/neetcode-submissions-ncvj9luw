class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        setNums = set(nums)
        sortedNums = sorted(setNums)

        output = 0
        streak = 0
        expected = None
        for i in range(len(sortedNums)):
            num = sortedNums[i]
            if num != expected:
                streak = 1
            expected = num + 1
            if streak > output:
                output = streak
            streak += 1

        return output


        