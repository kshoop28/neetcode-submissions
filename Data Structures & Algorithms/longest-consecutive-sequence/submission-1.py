class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        num_set = set(nums)
        longest = 0

        # cycle through every number
        for num in nums:
            count = 1  # current number itself
            next_num = num + 1

            # keep checking num+1, num+2, ... in the set
            while next_num in num_set:
                count += 1
                next_num += 1

            longest = max(longest, count)

        return longest
