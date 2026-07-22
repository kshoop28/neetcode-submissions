class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup = set(nums)
        dup = list(dup)
        if sorted(dup) == sorted(nums):
            return False
        else:
            return True