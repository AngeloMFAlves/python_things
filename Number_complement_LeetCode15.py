class Solution:
    def findComplement(self, num: int) -> int:
        bin_str = ''
        solution_str = ''
        int_solution = 0
        while num >= 1:
            bin_char = num%2
            bin_str += str(bin_char)
            num = num//2
        for i in bin_str:
            if i == '1':
                solution_str += '0'
            if i == '0':
                solution_str += '1'
        for i in range(len(solution_str)):
            int_solution += (int(solution_str[i])*2**i)
        return int_solution
