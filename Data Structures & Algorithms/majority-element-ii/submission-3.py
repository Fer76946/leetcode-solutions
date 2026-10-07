class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {}
        # step 1: count frequencies in O(n) time 
        for num in nums:
            count[num] = count.get(num, 0) + 1
        #step 2: collect
        res = []
        threshold = len(nums) // 3

        for num, c in count.items():
            if c > threshold:
                res.append(num)
        return res