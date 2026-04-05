class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = "".join(s.split("-")).upper()
        s = "-".join([s[max(i-k, 0):i] for i in range(len(s), 0, -k)][::-1])
        return s