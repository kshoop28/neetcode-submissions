import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minheap = []
        for i in range(k):
            heapq.heappush(minheap, nums[i])  # 👈 Push first k elements

        for i in range(k, len(nums)):
            if nums[i] > minheap[0]:
                heapq.heappushpop(minheap, nums[i])

        return minheap[0]


            
