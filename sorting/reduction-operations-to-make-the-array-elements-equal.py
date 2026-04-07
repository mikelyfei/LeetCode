class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        from collections import Counter
        nums.sort(reverse=True)
        counter = Counter(nums)
        
        times = 0
        for i, (k, v) in enumerate(counter.items()):
            if i == 0:
                largest = k
            else:
                counter[k] += counter[largest]
                times += counter[largest]
                counter[largest] = 0
                largest = k
        return times
