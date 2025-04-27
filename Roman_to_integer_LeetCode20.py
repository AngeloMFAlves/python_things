class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        previous = 0
        romans = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        for algarism in reversed(s):
            value = romans[algarism]
            if value < previous:
                result -= value
            else:
                result += value
            previous = value
        return result
            