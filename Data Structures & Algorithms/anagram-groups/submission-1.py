class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashs = defaultdict(list)
        for s in strs:
            count = [0] * 26 

            for c in s:
                count[ord(c) - ord('a')] += 1
            
            hashs[tuple(count)].append(s)

        return list(hashs.values())