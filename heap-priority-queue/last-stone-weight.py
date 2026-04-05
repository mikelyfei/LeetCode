class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            a = - heapq.heappop(stones)
            b = - heapq.heappop(stones)
            if a-b > 0:
                heapq.heappush(stones, b-a)
        return 0 if len(stones) == 0 else -stones[0]