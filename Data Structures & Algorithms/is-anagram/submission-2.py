class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        letters = {}
        for char in s:
            if char in letters: 
                letters[char]+=1
            else:
                letters.update({char: 1})
        for char in t:
            if char in letters:
                letters[char]-=1
                if letters[char] == 0:
                    letters.pop(char)
        
        if not letters:
            return True
        else:
            return False
            