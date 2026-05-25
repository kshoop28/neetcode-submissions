class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashmap = {}

        for index,value in enumerate(nums):
            compliment = target - value
            if compliment in hashmap:
                return [hashmap[compliment],index]
            else:
                hashmap[value] = index