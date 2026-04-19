class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        self.nums.sort(reverse=True)

    def add(self, val: int) -> int:
        # if val>self.nums[0]:
        #     self.nums = [val] + self.nums
        #     return self.nums[self.k-1]
        
        for i, num in enumerate(self.nums):
            if num<val:
                self.nums = self.nums[:i] + [val] + self.nums[i:]
                return self.nums[self.k-1]
        self.nums.append(val)
        return self.nums[self.k-1]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)