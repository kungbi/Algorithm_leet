

class Solution:
    def reverse(self, x: int) -> int:
        reversed = int(str(abs(x))[::-1])
        if not -(2**31) <= reversed <= 2**31 - 1:
            return 0
        return reversed if 0 <= x else reversed * -1