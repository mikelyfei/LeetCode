class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        ans = set()
        for q in queries:
            for d in dictionary:
                if len(q)!=len(d):
                    continue
                edits = 0
                n = len(q)
                for i in range(n):
                    if q[i]!=d[i]:
                        edits+=1
                    if edits>2:
                        break
                if edits<=2:
                    ans.add(q)
        return list(ans)
        