class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        for num in range(low,high+1):
            string = str(num)
            medium = (len(string))//2
            if len(string)%2 != 0:
                continue
            else:
                if sum(int(d) for d in string[:medium]) == sum(int(d) for d in string[medium:]):
                    count += 1
        return count