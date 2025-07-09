class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_string = str(x)
        palindrome_str = ''
        for i in x_string[::-1]:
            palindrome_str += i
        if palindrome_str == x_string:
            return True
        return False
