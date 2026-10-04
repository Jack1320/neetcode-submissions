class Solution:
    def findMin(self, nums: List[int]) -> int:
        #start at beginning, stop when decrease
        i = 0
        start = nums[0]

        if len(nums) == 1:
            return start

        if start < nums[-1]:
            return start

        while nums[i+1] > start:
            i+=1
        return nums[i+1]