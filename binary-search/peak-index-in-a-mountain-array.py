class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        arr.append(-float('inf'))
        l, r = 0, len(arr)
        while l<r:
            mid = l + (r-l)//2
            
            if arr[mid-1] < arr[mid] and arr[mid] > arr[mid+1]:
                return mid
            elif arr[mid-1] < arr[mid] < arr[mid+1]:
                l = mid + 1
            elif arr[mid-1] > arr[mid] > arr[mid+1]:
                r = mid
        return l