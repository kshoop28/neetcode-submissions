class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ls =[]
        count = 0
        nums.append(0)
        for num in nums:
            if num == 0:
                ls.append(count)
                count = 0
            elif num == 1:
                count += 1
        ls = max(ls)
            
        return ls

