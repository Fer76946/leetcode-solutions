class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        res = []

        for i in nums:
            if not res or i != res[-1]:
                res.append(i)
        nums[:len(res)] = res
        return len(res)