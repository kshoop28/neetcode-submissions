class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longs = 0
        for num in nums:

            if (num - 1) not in nums:
                lens = 1
                current = num

                while (current + 1) in nums:
                    lens += 1
                    current +=1 

                longs = max(longs, lens)

        return longs
                    




