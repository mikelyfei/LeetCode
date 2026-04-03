class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        i = 1
        res = []
        i_s = []
        for num in target:
            while num > i:
                res.append("Push")
                res.append('Pop')
                i += 1
            if num == i:
                res.append("Push")
                i += 1
        return res