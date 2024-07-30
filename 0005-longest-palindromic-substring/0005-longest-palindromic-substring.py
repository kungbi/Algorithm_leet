from collections import deque

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        queue = deque([(i, i) for i in range(n)])
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                queue.append((i, i + 1))

        tmp = deque()
        answer = ""
        while queue:
            a, b = queue.popleft()
            length = b - a + 1
            if len(answer) < length:
                answer = s[a: b + 1]

            if not (0 <= a - 1 and b + 1 < n):
                continue
            if s[a - 1] == s[b + 1]:
                queue.append((a - 1, b + 1))
        return answer
            