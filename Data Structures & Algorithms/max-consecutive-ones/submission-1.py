class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        couns = 0
        maxs = 0
        nums.append(0)
        for i in range(len(nums)):
            if nums[i] == 1:
                couns += 1
            elif nums[i] == 0:
                if couns > maxs:
                    maxs = 0
                    maxs += couns
                couns = 0 
        return maxs

