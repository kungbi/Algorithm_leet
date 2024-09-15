from collections import defaultdict

class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        n = len(s)

        mask = 0
        answer = 0
        mem_arr = {0: -1}

        for i in range(n):
            if s[i] == 'a':
                mask ^= 1
            elif s[i] == 'e':
                mask ^= 2
            elif s[i] == 'i':
                mask ^= 4
            elif s[i] == 'o':
                mask ^= 8
            elif s[i] == 'u':
                mask ^= 16
            
            print(mask)
            if mask not in mem_arr:
                mem_arr[mask] = i
            
            answer = max(answer, i - mem_arr[mask])

        return answer
            

