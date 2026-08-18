class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashs = set(nums)
        longest = 0

        for num in hashs:
            if num - 1 not in hashs:
                lens = 1
                curr = num
            
                while curr + 1 in hashs:
                    lens += 1
                    curr += 1
                
                longest = max(longest, lens)

        return longest
