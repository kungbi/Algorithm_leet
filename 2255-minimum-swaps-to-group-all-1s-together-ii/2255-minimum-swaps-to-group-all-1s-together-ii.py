class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        window = sum(nums)

        nums *= 2
        prefix_sum = [0] * (n*2)
        prefix_sum[0] = nums[0]

        for i in range(1, n * 2):
            prefix_sum[i] = prefix_sum[i-1] + nums[i]
        
        result = float('inf')
        for i in range(n):
            tmp_sum = prefix_sum[i + window - 1]
            tmp_sum -= prefix_sum[i - 1] if 0 <= i - 1 else 0
            zero_c = window - tmp_sum
            result = min(result, zero_c)

        return result
        