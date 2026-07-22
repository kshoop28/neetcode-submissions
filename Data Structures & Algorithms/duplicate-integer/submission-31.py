class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup = set(nums)
        if list(sorted(dup)) == sorted(nums):
            return False
        else:
            return True