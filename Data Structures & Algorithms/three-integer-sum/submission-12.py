class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        n = len(nums)
        
        output = []
        for i in range(n-2):
            if i>0 and nums[i] == nums[i-1]:
                continue
            
            j = i+1
            k = n-1
            target = -nums[i]
            while j<k:
                currentsum = nums[j] + nums[k]
                if currentsum == target:
                    output.append([nums[i], nums[j], nums[k]])
                    while nums[j] + nums[k] == currentsum and j<n-1:
                        j+=1
                elif currentsum > target:
                    k-=1
                else:
                    j+=1
        return output
                