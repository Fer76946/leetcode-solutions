class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashie = {}

        for i, n in enumerate(nums):
            complement = target - n
            if complement in hashie:
                return [hashie[complement], i]
            hashie[n] = i