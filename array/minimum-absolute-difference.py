class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_abs = float('inf')
        n = len(arr)
        res = []
        for i in range(1, n):
            if abs(arr[i] - arr[i-1]) < min_abs:
                res = [[arr[i-1], arr[i]]]
                min_abs = abs(arr[i] - arr[i-1])
            elif abs(arr[i] - arr[i-1]) == min_abs:
                res.append([arr[i-1], arr[i]])
        return res