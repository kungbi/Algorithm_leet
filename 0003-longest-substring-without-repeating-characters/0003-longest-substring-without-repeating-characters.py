from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = right = 0
        n = len(s)
        counter = defaultdict(int)
        max_length = 0
        while left < n and right < n:
            if counter[s[right]] == 0:
                counter[s[right]] += 1
                right += 1
                if max_length < right - left:
                    max_length = right - left
            else:
                counter[s[left]] -= 1
                left += 1
        return max_length
            
