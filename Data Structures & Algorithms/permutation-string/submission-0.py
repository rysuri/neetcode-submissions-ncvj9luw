class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        freqs1 = {}
        freqs2 = {}

        for i in range(len(s1)):
            freqs1[s1[i]] = 1 + freqs1.get(s1[i],0)
            freqs2[s2[i]] = 1 + freqs2.get(s2[i],0)
        
        if freqs1 == freqs2:
            return True

        l = 0
        for r in range(len(s1), len(s2)):
            freqs2[s2[r]] = 1 + freqs2.get(s2[r], 0)
            freqs2[s2[l]] -= 1
            if freqs2[s2[l]] == 0:
                del freqs2[s2[l]]
            l += 1
            if freqs1 == freqs2:
                return True
        return False

