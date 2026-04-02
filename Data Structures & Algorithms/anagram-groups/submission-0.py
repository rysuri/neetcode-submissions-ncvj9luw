
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for string in strs:
            count = [0] * 26 # [0,0,0,0,0,0,0,...,0]

            for char in string:
                count[ord(char) - ord("a")] += 1# gets ascii value of c. 
            
            res[tuple(count)].append(string)

        return list(res.values())