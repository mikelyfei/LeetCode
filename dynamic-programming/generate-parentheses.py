class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        path = []
        def dfs(l, r):
            if l==0 and r==0:
                res.append("".join(path))
            if l>0:
                path.append("(")
                dfs(l-1, r)
                path.pop()

            if r>l:
                path.append(")")
                dfs(l, r-1)
                path.pop()
        dfs(n, n)            
        return res