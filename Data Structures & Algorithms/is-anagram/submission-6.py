class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #they are anagrams if they have the same num of each letter.
        #could i make a dict for each that stores the number with the letter and then see if dicts are equal
        dict1 = {chr(i):0 for i in range (ord("a"), ord("z")+1)}
        dict2 = {chr(i):0 for i in range (ord("a"), ord("z")+1)}

        for i in s:
            dict1[i] += 1
        for j in t:
            dict2[j] += 1
        if dict1 == dict2:
            return True
        else:
            return False
    