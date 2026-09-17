class Solution:
    def isPalindrome(self, s: str) -> bool:
        # build into an array not including non alphanumeric
        stringarr = []

        for i in s:
            if i.isalnum():
                stringarr.append(i.lower())

        n = len(stringarr)
        middle = -1
        if n % 2 == 1:
            middle = int(n/2)

        tracker = []
        for i in range(n):
            if stringarr[i].isalnum() and i != middle:
                if tracker and stringarr[i] == tracker[-1]:
                    tracker.pop()
                else:
                    tracker.append(stringarr[i])
        return tracker == []
            