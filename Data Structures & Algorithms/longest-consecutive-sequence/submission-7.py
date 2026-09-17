class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        
        inArray = set(nums)
        
        tracker = []
        for i in nums:
            if i-1 in inArray:
               continue                
            count = 1
            j = i
            while (j+1) in inArray:
                count+=1
                j+=1
            tracker.append(count)
        return max(tracker)
