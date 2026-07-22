class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sls, tls, = s, t
        sls = sorted(sls)
        tls = sorted(tls)
        if tls == sls:
            return True
        else:
            return False

