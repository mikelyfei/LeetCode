class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        if target not in words:
            return -1
        n = len(words)
        ans = float('inf')
        for i, word in enumerate(words):
            if word == target:
                targetIndex = i
                ans = min(ans, min(abs(targetIndex - startIndex) % n, abs(n-max(targetIndex, startIndex) + min(startIndex, targetIndex)) % n))
        return ans