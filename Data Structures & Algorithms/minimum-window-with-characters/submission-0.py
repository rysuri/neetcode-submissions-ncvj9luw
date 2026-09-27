class Solution:


    def minWindow(self, s: str, t: str) -> str:
        
        # Create frequency table for string t.
        freqt = {}
        # Create frequency table for string s, initialized all to 0.
        freqs = {}

        for char in t:
            freqt[char] = 1 + freqt.get(char, 0)
            freqs[char] = 0

        left = 0
        best_left = 0
        smallestSolution = float('inf')
        have = 0
        need = len(freqt)
        
        for right in range(len(s)):
            rightCharacter = s[right]

            if rightCharacter in freqt:
                freqs[rightCharacter] += 1
                if freqs[rightCharacter] == freqt[rightCharacter]:
                    have += 1
            
            while have == need:
                if (right - left + 1) < smallestSolution:
                    smallestSolution = right - left + 1
                    best_left = left
                
                leftCharacter = s[left]
                if leftCharacter in freqt:
                    freqs[leftCharacter] -= 1
                    if freqs[leftCharacter] < freqt[leftCharacter]:
                        have -= 1
                left += 1
                
        return s[best_left:best_left + smallestSolution] if smallestSolution != float('inf') else ""