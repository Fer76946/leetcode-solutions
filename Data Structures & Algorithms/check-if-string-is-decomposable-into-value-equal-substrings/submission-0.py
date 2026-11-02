class Solution:
    def isDecomposable(self, s: str) -> bool:
        has_two = False
        i = 0
        n = len(s)
        while i < n:
            count = 0
            char = s[i]
            while i < n and s[i] == char:
                count += 1
                i += 1
            if count % 3 == 1:
                return False
            elif count % 3 == 2:
                if has_two:
                    return False
                has_two = True
        return has_two