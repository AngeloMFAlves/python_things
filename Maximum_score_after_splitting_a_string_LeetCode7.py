class Solution:
    def maxScore(self, s: str) -> int:
        max_score = 0
        for i in range(1,len(s)):
            sum_split = int(s[:i].count('0')) + int(s[i:].count('1'))
            if sum_split > max_score:
                max_score = sum_split
        return max_score