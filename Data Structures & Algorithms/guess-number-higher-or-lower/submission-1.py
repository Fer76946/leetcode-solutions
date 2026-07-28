# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l = 1
        while l <= n:
            mid = (l + n) // 2
            res = guess(mid)

            if res == 0:
                return mid
            elif res < 0:
                n = mid - 1
            else:
                l = mid + 1