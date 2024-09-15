from collections import defaultdict

class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        n = len(s)

        mask = 0
        answer = 0
        mem_arr = {0: -1}
        vowels = {'a': 1, 'e': 2, 'i': 4, 'o': 8, 'u': 16}

        for i in range(n):
            if s[i] in vowels:
                mask ^= vowels[s[i]]
            
            print(mask)
            if mask not in mem_arr:
                mem_arr[mask] = i
            
            answer = max(answer, i - mem_arr[mask])

        return answer
            

