class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # take a product of all entries in num, 
        # and product the output array by dividing by nums[i]
        
        #first find out how many zeros (zero, one, more than 1)
        zeroCount = 0
        numsProd = 1
        zeroPlace = []
        n = len(nums)

        for i in range(n):
            if nums[i] == 0:
                zeroCount += 1
                zeroPlace.append(i)
            else:
                numsProd *= nums[i]
        
        output = []
        if zeroCount > 1:
            output = [0]*n
            return output
        elif zeroCount == 1:
            output = [0]*n
            output[zeroPlace[0]] = numsProd
            return output
        else:
            for i in range(n):
                output.append(int(numsProd/nums[i]))
            return output