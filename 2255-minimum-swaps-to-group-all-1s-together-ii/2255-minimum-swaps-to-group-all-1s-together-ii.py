class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        window = sum(nums)

        result = count = sum(nums[0:window])
        nums *= 2

        for i in range(1, n):
            count -= nums[i-1]
            count += nums[i + window - 1]
            result = max(result, count)

        return window - result
        