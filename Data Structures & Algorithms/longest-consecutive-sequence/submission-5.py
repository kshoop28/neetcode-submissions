class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        num_set = set(nums)
        longest = 0

        for num in nums:
            sequence = [num]  # start a new consecutive list
            next_num = num + 1

            # keep adding next numbers if they exist
            while next_num in num_set:
                sequence.append(next_num)
                next_num += 1

            # update longest if this sequence is bigger
            longest = max(longest, len(sequence))

        return longest
