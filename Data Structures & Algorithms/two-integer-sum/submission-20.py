class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}

        for i, n in enumerate(nums):
            my_dict[n] = i
        
        for j, n in enumerate(my_dict):
            diff = target - n
            if diff in my_dict and j != my_dict[diff]:
                return [j, my_dict[diff]]
            else:
                continue

        # Create a hashmap
        # The keys would be the index in nums
        # The values then would be num
        # Then we loop over the hashmap to see if the value of each equals any of the other keys
        # We then return the index as an array is the underlying data strucutre of a hashmap




        