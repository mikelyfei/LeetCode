class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        if not b:
            return 0
        m = len(a)
        n = len(b)
        k = ceil(n/m)
        if b in a*k:
            return k
        if b in a*(k+1):
            return k+1
        return -1