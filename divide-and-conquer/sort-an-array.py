class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge_sort(nums, l, r):
            if l==r:
                return [nums[l]]
            mid = l + (r-l)//2
            left = merge_sort(nums, l, mid)
            right = merge_sort(nums, mid+1, r)
            return merge(left, right)
        def merge(arr1, arr2):
            if arr1 and not arr2:
                return arr1
            elif not arr1 and arr2:
                return arr2
            elif not arr1 and not arr2:
                return []
            n1, n2 = len(arr1), len(arr2)
            res = []
            i, j = 0, 0
            while i<n1 and j<n2:
                if arr1[i] <= arr2[j]:
                    res.append(arr1[i])
                    i+=1
                else:
                    res.append(arr2[j])
                    j+=1
            if i>=n1 and j<n2:
                res.extend(arr2[j:])
            if j>=n2 and i<n1:
                res.extend(arr1[i:])
            return res
        return merge_sort(nums, 0, len(nums)-1)
