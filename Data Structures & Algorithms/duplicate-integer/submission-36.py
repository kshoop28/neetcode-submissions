class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashs = {}

        for num in nums:
            if num in hashs:
                hashs[num] += 1
            else:
                hashs[num] = 1
            if hashs[num] > 1:
                return True
        return False
    