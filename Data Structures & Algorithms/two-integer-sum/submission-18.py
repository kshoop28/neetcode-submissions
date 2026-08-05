class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}

        for i in range(len(nums)):
            my_dict[nums[i]] = target - nums[i] 
            for j, key in enumerate(my_dict):
                if i != j: 
                    if key == my_dict[nums[i]]: 
                        return [j, i]


            

        # Create a hashmap
        # The keys would be the numbers in num
        # The values then would be the target - the numbers
        # Then we loop over the hashmap to see if the value of each equals any of the other keys
        # We then return the index as an array is the underlying data strucutre of a hashmap




        