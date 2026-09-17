class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # use the set data structure
        s = set()
        for i in nums:
            s.add(i)
        if len(s) == len(nums):
            return False
        else:
            return True