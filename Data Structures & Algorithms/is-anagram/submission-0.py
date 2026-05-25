class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        self.s = s
        self.t = t

        sorted_words = sorted(s)
        sorted_wordt = sorted(t)

        if sorted_words == sorted_wordt:
            return True
        else:
            return False
        
        