from collections import defaultdict

class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        n = len(s)

        mask = 0
        answer = 0
        mem_arr = [-1] * (2**5 + 1)

        for i in range(n):
            if s[i] == 'a':
                mask ^= 1 << 0
            elif s[i] == 'e':
                mask ^= 1 << 1
            elif s[i] == 'i':
                mask ^= 1 << 2
            elif s[i] == 'o':
                mask ^= 1 << 3
            elif s[i] == 'u':
                mask ^= 1 << 4
            
            if mem_arr[mask] == -1 and 0 < mask:
                mem_arr[mask] = i
            else:
                answer = max(answer, i - mem_arr[mask])

        return answer
            

