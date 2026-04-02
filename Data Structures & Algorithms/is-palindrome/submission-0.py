class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            leftChar = s[l]
            rightChar = s[r]

            if leftChar.lower() != rightChar.lower():
                if not leftChar.isalnum():
                    l += 1
                    continue
                if not rightChar.isalnum():
                    r -= 1
                    continue
                return False

            l += 1
            r -= 1

        return True