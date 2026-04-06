class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        n = len(nums)
        even = [0]*n
        odd = [0]*n
        even[0] = nums[0]
        for i in range(1,n):
            even[i] = even[i-1]
            odd[i] = odd[i-1]
            if i%2:
                odd[i]+=nums[i]
            else:
                even[i]+=nums[i]
        
        ans=0
        for i in range(n):
            even_left = even[i-1] if i>0 else 0
            odd_left = odd[i-1] if i>0 else 0
            even_right = odd[-1] - odd[i]
            odd_right = even[-1] - even[i]
            if even_left + even_right == odd_left + odd_right:
                ans+=1
        return ans 