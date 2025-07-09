class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count_pref = 0
        for word in words:
            if word.startswith(pref) == True:
                count_pref += 1
        return count_pref