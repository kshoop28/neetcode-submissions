class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashs = {}
        mapss = {}

        for let in s:
            if let not in hashs:
                hashs[let] = 1
            else:
                hashs[let] += 1

        for let in t:
            if let not in mapss:
                mapss[let] = 1
            else:
                mapss[let] += 1
        if hashs == mapss:
            return True
        else:
            return False
        