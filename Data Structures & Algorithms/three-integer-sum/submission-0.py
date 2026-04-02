class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        result = set()
        a = 0
        b = 1
        c = len(nums) - 1

        for i in range(len(nums)):
            while c > b:
                if (nums[a] + nums[b] + nums[c]) > 0:
                    c-=1
                elif (nums[a] + nums[b] + nums[c]) == 0:
                    result.add((nums[a], nums[b], nums[c]))
                    b+=1
                    c-=1
                elif (nums[a] + nums[b] + nums[c]) < 0:
                    b+=1
            a+=1
            b = a+1
            c=len(nums)-1
        return[list(sol) for sol in result]

        