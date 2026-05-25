class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
# 1. Count frequencies
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1

        # 2. Create buckets
        buckets = [[] for _ in range(len(nums) + 1)]

        # 3. Fill buckets
        for num, freq in count.items():
            buckets[freq].append(num)

        # 4. Collect top k
        res = []
        for i in range(len(buckets) - 1, -1, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res