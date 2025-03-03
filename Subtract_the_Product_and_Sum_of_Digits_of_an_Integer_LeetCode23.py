class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        sum_alg = 0
        for i in str(n):
            product *= int(i)
            sum_alg += int(i)
        return product - sum_alg