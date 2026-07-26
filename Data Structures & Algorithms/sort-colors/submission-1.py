class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        if n == 0:
            return nums
        buckets = []
        for i in range(len(nums)):
            buckets.append([])
        max_val = max(nums)
        for num in nums:
            norm = num / (max_val + 1)
            bucketnum = int(norm)
            buckets[bucketnum].append(num)
        for bucket in buckets:
            for a in range(1, len(bucket)):
                b = a
                while b > 0 and bucket[b-1] > bucket[b]:
                    bucket[b - 1], bucket[b] = bucket[b], bucket[b-1]
                    b -= 1
        idx = 0
        for bucket in buckets:
            for num in bucket:
                nums[idx] = num
                idx += 1


        """
        Do not return anything, modify nums in-place instead.
        """
        