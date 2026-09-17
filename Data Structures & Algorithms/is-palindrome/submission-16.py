class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        left = 0
        right = n - 1

        while left < right:
            while not s[left].isalnum() and left < n-1:
                left += 1
            while not s[right].isalnum() and right > 0:
                right -= 1
            if s[left].lower() != s[right].lower() and s[left].isalnum() and s[right].isalnum():
                return False
            left += 1
            right -=1
        return True

            