class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for i in strs:
            string += str(len(i))+"#"+i
        return string

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        j = 0
        while i < len(s):
            if s[i] == "#":
                length = int(s[j:i])
                strs.append(s[i+1:i+length+1])
                i += length+1
                j = i
            else:
                i += 1
        return strs




        

