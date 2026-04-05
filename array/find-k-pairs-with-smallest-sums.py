class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        import heapq
        heap = []
        n1 = len(nums1)
        n2 = len(nums2)
        for i in range(min(k, n1)):
            heapq.heappush(heap, (nums1[i]+nums2[0], i, 0))
        ans = []
        while heap and len(ans) < k:
            _, i, j = heapq.heappop(heap)
            ans.append([nums1[i], nums2[j]])
            if j+1 < n2:
                heapq.heappush(heap, (nums1[i]+nums2[j+1], i, j+1))
        return ans