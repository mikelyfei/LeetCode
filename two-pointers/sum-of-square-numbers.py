class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        import math
        a, b = 1, math.ceil(math.sqrt(c))
        while a<=b:
            mid = a+(b-a)//2
            if a**2+mid**2>c:
                b-=1
            elif a**2+mid**2<c:
                a+=1
            else:
                return True
        return False
            