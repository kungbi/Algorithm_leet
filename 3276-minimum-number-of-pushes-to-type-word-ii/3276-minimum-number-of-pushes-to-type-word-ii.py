from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:
        counted = Counter(word)
        numbers = {}

        i = 0
        for c, t in counted.most_common():
            numbers[c] = i // 8 + 1
            i += 1

        result = 0
        for c in word:
            result += numbers[c]
        return result