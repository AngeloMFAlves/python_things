class Solution:
    def reverse(self, x: int) -> int:
        list_num = [num for num in str(x)]
        result = ''
        if list_num[0] == '-':
            result += '-'
        for num in list_num[::-1]:
            if num == '-':
                continue
            result += num
        if int(result) < (-2)**31:
            return 0
        if int(result) > (2**31-1):
            return 0
        return int(result)