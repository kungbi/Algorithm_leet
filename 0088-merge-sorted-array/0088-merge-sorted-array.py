class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        array = []
        for i in range(m):
            array.append(nums1[i])
        for i in range(n):
            array.append(nums2[i])

        array.sort()
        for i in range(m + n):
            nums1[i] = array[i]
                
        