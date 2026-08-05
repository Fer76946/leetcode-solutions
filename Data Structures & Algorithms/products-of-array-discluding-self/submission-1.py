class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for idx, n in enumerate(nums):
            res = 1
            for i_idx, i in enumerate(nums):
                if i_idx != idx:
                    res = res * i
            output.append(res)
        return output
