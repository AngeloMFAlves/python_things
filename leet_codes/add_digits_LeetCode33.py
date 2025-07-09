def addDigits(self, num: int) -> int:
    result = 0
    if len(str(num)) == 1:
        return num
    for i in str(num):
        result += int(i)
    return self.addDigits(result)
