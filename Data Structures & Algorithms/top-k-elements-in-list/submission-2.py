class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count frequency of each number
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        # Step 2: Create buckets where index = frequency
        buckets = [[] for _ in range(len(nums) + 1)]

        # Step 3: Fill the buckets
        for num, freq in count.items():
            buckets[freq].append(num)

        # Step 4: Collect results from most frequent → least frequent
        res = []
        for i in range(len(buckets) - 1, 0, -1):
            if not buckets[i]:        # ✅ Explicitly skip empty buckets
                continue              # Move to the next frequency

            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
