class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        import random
        def quick_sort(nums, left, right):
            if left >= right:
                return
            idx = random.randint(left, right)
            nums[left], nums[idx] = nums[idx], nums[left]
            pivot = nums[left]
            l, r = left, right
            while l<r:
                while l<r and nums[r]>=pivot:
                    r-=1
                while l<r and nums[l]<=pivot:
                    l+=1
                nums[l], nums[r] = nums[r], nums[l]
            nums[left], nums[l] = nums[l], nums[left]
            quick_sort(nums, left, l-1)
            quick_sort(nums, l+1, right)
        quick_sort(nums, 0, len(nums)-1)
        return nums