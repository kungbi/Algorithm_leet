class Solution:
    def countSeniors(self, details: List[str]) -> int:
        result = 0
        for line in details:
            if 60 < int(line[11:13]):
                result += 1
        return result