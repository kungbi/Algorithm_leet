class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        n = len(a)
        s_list = []

        l, r = 0, n - 1
        while l < r and a[l] == b[r]:
            l, r = l + 1, r - 1
        s_list.append(a[l:r + 1])
        s_list.append(b[l:r + 1])

        l, r = 0, n - 1
        while l < r and b[l] == a[r]:
            l, r = l + 1, r - 1
        s_list.append(a[l:r + 1])
        s_list.append(b[l:r + 1])

        for s in s_list:
            if s == s[::-1]:
                return True
        return False



