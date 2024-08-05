class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        

        count = 0
        prev_c = ''

        left = right = 0
        while right < n:
            if prev_c != nums[right]:
                print(left, right)
                prev_c = nums[right]
                nums[left] = nums[right]
                left, right = left + 1, right + 1
                count = 1
            else:
                if count < 2:
                    nums[left] = nums[right]
                    left += 1
                right += 1
                count += 1

        return left



        