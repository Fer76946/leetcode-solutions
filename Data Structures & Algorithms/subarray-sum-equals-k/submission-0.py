class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        sum = 0
        prefix_sums = {0: 1}

        for num in nums:
            sum += num
            if sum - k in prefix_sums:
                count += prefix_sums[sum - k]
            prefix_sums[sum] = prefix_sums.get(sum, 0) + 1

        return count