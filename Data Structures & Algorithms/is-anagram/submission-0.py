class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictionary = {}
        if len(s) != len(t): return False
        
        for letter in s:
            if letter not in dictionary:
                dictionary.setdefault(letter, 1)
            else:
                dictionary[letter] += 1
        
        for letter in t:
            if letter not in dictionary:
                return False
            else:
                dictionary[letter] -=1
        
        for value in dictionary.values():
            if value != 0: return False
        
        return True

        

        