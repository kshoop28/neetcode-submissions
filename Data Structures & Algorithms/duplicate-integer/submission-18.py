class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ls = set([])
        for num in range(len(nums)):
            if nums[num] in ls:
                return True
            ls.add(nums[num])

        return False
            