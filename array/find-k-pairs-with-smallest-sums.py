class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        import heapq
        heap = []
        for n1 in nums1:
            for n2 in nums2:
                heapq.heappush(heap, (n1+n2, n1, n2))
        ans = []
        for i in range(k):
            s, n1, n2 = heapq.heappop(heap)
            ans.append([n1, n2])
        return ans