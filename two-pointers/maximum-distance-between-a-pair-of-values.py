class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        n1 = len(nums1)
        n2 = len(nums2)
        ans = 0
        for i in range(n1):
            l = i
            if i > n2-1:
                break
            r = n2 
            while l<r:
                mid = (l + r) // 2
                if nums2[mid] >= nums1[i]:
                    l = mid + 1
                else:
                    r = mid
            ans = max(ans, l - 1 - i)
        return ans