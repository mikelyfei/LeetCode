class Solution:
    def magicalString(self, n: int) -> int:
        i = 2
        s = [1, 2, 2]
        while len(s) < n:
            s += [3-s[-1]]*s[i]
            i += 1
        return s[:n].count(1)