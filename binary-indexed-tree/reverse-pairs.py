class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge_sort(l, r):
            if r - l <= 1:
                return 0

            mid = (l + r) // 2
            count = merge_sort(l, mid) + merge_sort(mid, r)

            # count cross pairs
            j = mid
            for i in range(l, mid):
                while j < r and nums[i] > 2 * nums[j]:
                    j += 1
                count += j - mid

            # merge
            temp = []
            i, j = l, mid
            while i < mid and j < r:
                if nums[i] <= nums[j]:
                    temp.append(nums[i])
                    i += 1
                else:
                    temp.append(nums[j])
                    j += 1

            temp.extend(nums[i:mid])
            temp.extend(nums[j:r])

            nums[l:r] = temp
            return count

        return merge_sort(0, len(nums))