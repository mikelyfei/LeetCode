class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        if n==1:
            return [1]
        if n==2:
            return range(1, 2)
        odd_arr = [x*2-1 for x in self.beautifulArray((n+1)//2)]
        even_arr = [x*2 for x in self.beautifulArray(n//2)]
        return odd_arr + even_arr
