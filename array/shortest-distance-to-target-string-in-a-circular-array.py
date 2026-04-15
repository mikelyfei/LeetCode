class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        try:
            targetIndex = words.index(target)
        except ValueError:
            return -1
        n = len(words)
        return min(abs(targetIndex - startIndex) % n, abs(n-targetIndex + startIndex) % n)