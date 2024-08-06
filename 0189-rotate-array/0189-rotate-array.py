class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)

        if n < k:
            k %= n
        
        
        left = 0
        right = n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left, right = left + 1, right - 1

        left = 0
        right = k - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left, right = left + 1, right - 1

        left = k
        right = n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left, right = left + 1, right - 1


        
        return 0


        