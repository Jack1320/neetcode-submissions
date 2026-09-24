class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_dict = dict()
        s_dict = dict() # the window
        l = 0
        best_slice = [0,float("inf")]
        """
        for r in range(len(s)):
            while valid:
                update index if best
                shrink from left
        return s[best_slice[0]:best_slice[1]]    
        """
        for i in t:
            t_dict[i] = 1 + t_dict.get(i,0)

        def valid(s_dict, t_dict): #should run in constant time, though not O(1)
            for i in t_dict:
                if t_dict[i]>s_dict.get(i,0):
                    return False
            return True

        for r in range(len(s)):
            s_dict[s[r]] = 1 + s_dict.get(s[r],0)

            while valid(s_dict, t_dict):
                if r-l<best_slice[1]-best_slice[0]:
                    best_slice[0] = l
                    best_slice[1] = r
                s_dict[s[l]] -= 1
                l+=1
        if best_slice[1] != float("inf"):
            return s[best_slice[0]: best_slice[1]+1]
        else:
            return ""

