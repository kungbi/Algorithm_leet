from copy import deepcopy

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = deepcopy(nums)

        for i in range(n):
            a = b = 0
            if 0 <= i - 3:
                a = dp[i-3]
            if 0 <= i - 2:
                b = dp[i-2]
            dp[i] += max(a, b)
        return max(dp)

            