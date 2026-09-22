class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        chrset = set()
        maxlength = 0

        for r in range(len(s)):
            while s[r] in chrset:
                chrset.discard(s[l])
                l+=1
            chrset.add(s[r])
            length = len(chrset)
            if length>maxlength:
                maxlength = length
        return maxlength 