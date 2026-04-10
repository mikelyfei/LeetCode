class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        import heapq
        for num in nums:
            heapq.heappush(heap, -num)
        for i in range(k):
            ans = - heapq.heappop(heap)
        return ans