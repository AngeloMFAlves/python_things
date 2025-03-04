class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n > 1:
            power = n%3
            if power not in (0,1):
                return False
            n //= 3
        return True