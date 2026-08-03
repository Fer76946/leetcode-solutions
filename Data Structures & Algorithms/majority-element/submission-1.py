class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        majPoint = n / 2

        for i in nums:
            count = 0
            curr = i
            count += 1
            for j in nums:
                if j == curr:
                    count += 1
            if count > majPoint:
                return i