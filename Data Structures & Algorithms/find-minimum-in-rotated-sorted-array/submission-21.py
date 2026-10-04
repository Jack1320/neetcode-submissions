class Solution:
    def findMin(self, nums: List[int]) -> int:
        # find which half of the list the min is in
        # then find which hald of that new list the min is in etc
        # basically two pointers

        lo = 0
        hi = len(nums)-1
        
        while lo<hi:
            mid = (lo+hi)//2
            if nums[mid] < nums[hi]:
                hi = mid
            else:
                lo = mid+1
        return nums[lo]
