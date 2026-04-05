class Solution:
    def maskPII(self, s: str) -> str:
        if "@" in s:
            name, ext = s.split("@")
            name = name[0].lower() + "*****" + name[-1].lower()
            return name + "@" + ext.lower()
        s = s.replace("(", "").replace(")", "").replace("+", "").replace("-", "")
        flag = len(s)==10
        last4 = s[-4:]
        prev = "*" * (len(s)-4)
        prev = "-".join([prev[max(0, i-3):i] for i in range(len(prev), 0, -3)][::-1])
        prefix = "" if flag else "+"
        return prefix + prev + "-" + last4