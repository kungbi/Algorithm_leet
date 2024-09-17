class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        n = len(timePoints)
        timeList = [0] * n

        for i in range(n):
            h, m = map(int, timePoints[i].split(':'))
            timeList[i] = h * 60 + m
        timeList.sort()

        answer = float('inf')
        for i in range(n - 1):
            answer = min(answer, timeList[i + 1] - timeList[i])
        answer = min(answer, timeList[0] + 1440 - timeList[n - 1])

        return answer
        