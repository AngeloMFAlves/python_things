class Solution:
    def isPalindrome(self, s: str) -> bool:
        phrase_lower = s.lower()
        s_comp = ''
        str_conv = ''
        aux_list = []
        for i in phrase_lower:
            if i.isalpha() == False and i.isnumeric() == False:
                continue
            else:
                aux_list.append(i)
        for i in aux_list:
            s_comp += i
        for i in aux_list[::-1]:
            str_conv += i
        if str_conv == s_comp:
            return True
        else:
            return False

        