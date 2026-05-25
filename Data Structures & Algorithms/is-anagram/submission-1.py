class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        Jag = sorted(s)
        Qag = sorted(t)
        if Jag == Qag:
            return True
        else:
            return False

