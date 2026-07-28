class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for index, value in enumerate(nums):
            if nums[index] != val:
                nums[k] = nums[index]
                k += 1
        return k