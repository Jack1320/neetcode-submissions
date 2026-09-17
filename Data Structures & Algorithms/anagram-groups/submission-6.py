class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for i, string in enumerate(strs):
            # turn the string into a dict representing its characters
            # then turn the dicts values into a tuple which is hashable
            # add the tuple to the dict seen {tuple:string array} if its not already in there
            # if it is already in there, just update the string array to include the ith string
            # at the end, the keys in seen will group together the anagrams, we just loop through the dict

            dicti = {chr(j):0 for j in range(ord("a"), ord("z")+1)}
            for c in string:
                dicti[c] += 1
            
            stringtuple = tuple(dicti.values())

            if stringtuple in seen:
                seen[stringtuple].append(string)
            else:
                seen[stringtuple] = [string] 
        
        answer = []
        for keys in seen:
            answer.append(seen[keys])
        return answer    
