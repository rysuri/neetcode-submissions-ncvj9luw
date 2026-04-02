class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        hashmap = {}
        longest = 0
        l = 0

        for char in s:
            while char in hashmap:
                hashmap.pop(s[l])
                l = l + 1

            hashmap[char] = 1

            longest = max(longest, len(hashmap))

        return longest
                





        