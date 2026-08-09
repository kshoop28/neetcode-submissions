class Solution:
    def countBits(self, n: int) -> List[int]:

        ls = []

        for i in range(n + 1):
            count = 0
            while i > 0:
                if i & 1 == 1:
                    count += 1
                i = i >> 1
            ls.append(count)
        return ls
# The space complexity of this is O(n + 1) or just O(n) as we do not care about constants
# The time complexity of this is O(n log(n)) 


