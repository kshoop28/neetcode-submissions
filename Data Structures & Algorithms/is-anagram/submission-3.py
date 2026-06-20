class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ss = []
        tt = []
        for i in range(len(s)):
            ss.append(s[i])
        for j in range(len(t)):
            tt.append(t[j])
        ss.sort()
        tt.sort()
        if ss == tt:
            return True
        else:
            return False

