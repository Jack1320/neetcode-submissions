class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1]*n

        # updating to prefix array
        for i in range(1,n):
            output[i] = nums[i-1]*output[i-1]
        
        # updating to postfix array
        postfixMultiplier = 1
        for i in range(n-1,-1,-1):
            output[i] *= postfixMultiplier
            postfixMultiplier *= nums[i]
        return output
        
        