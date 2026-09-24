class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""
        l = 0
        s_dict = {}
        t_dict = {}
        best_slice, best_length = [0,0], float("inf")

        for i in t:
            t_dict[i] = 1 + t_dict.get(i,0)

        need = len(t_dict)
        have = 0

        for r in range(len(s)):
            c = s[r]
            s_dict[c] = 1 + s_dict.get(c,0)
            
            if c in t_dict and s_dict[c] == t_dict[c]:
                    have +=1

            while have == need:
                if (r-l+1)<best_length:
                    best_slice =[l,r]
                    best_length = r-l+1
                
                s_dict[s[l]] -= 1

                if s[l] in t_dict and s_dict[s[l]]<t_dict[s[l]]:
                    have-=1
                l+=1
        return s[best_slice[0]: best_slice[1]+1] if best_length != float("inf") else ""
                






