class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup = list(set(nums))
        if sorted(dup) == sorted(nums):
            return False
        else:
            return True