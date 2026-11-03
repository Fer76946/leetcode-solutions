class Solution:
    def removeVowels(self, s: str) -> str:

        newS = []
        vowels = ["a", "e", "i", "o", "u"]
        if not any(c in vowels for c in s):
            return s
        for l in s:
            if l not in vowels:
                newS.append(l)
        vowelLess = "".join(newS)
        return vowelLess
