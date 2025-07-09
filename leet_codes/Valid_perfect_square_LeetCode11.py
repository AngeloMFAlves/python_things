class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i = 0
        perf_sqr = False
        while i*i <= num:
            perf_sqr
            i+=1
            if i*i == num:
                perf_sqr = True
        return perf_sqr