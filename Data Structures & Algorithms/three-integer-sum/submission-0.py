class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
         # [2, 2, 3, 5, 6]
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]: #this checks for duplicates
                continue        #jumps to top and tries a different value
            
            # now use separate points, left and right, keep closing, either left or right

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res
