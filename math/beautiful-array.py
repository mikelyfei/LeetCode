class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        if n<=2:
            return list(range(1, n+1))
        odd_arr = [x*2-1 for x in self.beautifulArray((n+1)//2)]
        even_arr = [x*2 for x in self.beautifulArray(n//2)]
        return odd_arr + even_arr
