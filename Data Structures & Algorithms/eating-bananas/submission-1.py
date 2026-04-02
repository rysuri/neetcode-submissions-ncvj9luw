class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        mink = max(piles)

        while l <= r:
            k = l + ((r-l) // 2)
            totaleat = 0
            for pile in piles:
                totaleat = totaleat + -(-pile//k)
            
            if totaleat > h:
                l = k + 1
            else:
                r = k - 1
            
            if totaleat <= h:
                mink = min(k, mink)
        return mink
                



        