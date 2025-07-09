class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        aux = [i for i in s]
        if len(s) != len(t):
            return False
        for i in range(len(t)):
            if t[i] in aux:
                aux.remove(t[i])
                continue
            else:
                return False
        return True