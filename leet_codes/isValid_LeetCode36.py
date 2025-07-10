class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        symb = {
            "}" : "{",
            ")" : "(",
            "]" : "["
        }
        for ch in s:
            if ch in symb.values():
                stack.append(ch)
            elif ch in symb:
                if not stack or stack[-1] != symb[ch]:
                    return False
                stack.pop()
        return not stack
