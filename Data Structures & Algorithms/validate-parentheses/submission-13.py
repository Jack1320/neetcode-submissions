class Solution:
    def isValid(self, s: str) -> bool:
        tracker = [] # contains open parenthesis
        checker = {"}" : "{", ")" : "(", "]" : "["}
        
        for char in s:
            if char in checker:
                if tracker and tracker[-1] == checker[char]:
                    tracker.pop(-1)
                else:
                    return False 
            else:
                tracker.append(char)
        
        return tracker == []