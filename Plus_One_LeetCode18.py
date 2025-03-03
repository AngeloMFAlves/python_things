class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        str_aux = ''
        for number in digits:
            str_aux += str(number)
        int_number = int(str_aux)
        result_int = int_number + 1
        result_str = str(result_int)
        result = [int(number) for number in result_str]
        return result