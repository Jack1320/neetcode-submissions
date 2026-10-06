class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0
        r = len(nums)-1

        # reminder that len list is O(1)
        while r>l:
            m = (r+l)//2

            if nums[m]<nums[r]:
                if nums[m]<target<=nums[r]:
                    l=m+1
                else:
                    r = m
            else:
                if nums[l]<=target<=nums[m]:
                    r = m
                else:
                    l = m+1
        return r if nums[r] == target else -1