class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        length = len(nums)

        dict1 = {nums[i]: i for i in range(length) }

        for i in range(length):
            complement = target - nums[i]

            if complement in dict1 and dict1[complement] != i:
                return [i, dict1[complement]]
        