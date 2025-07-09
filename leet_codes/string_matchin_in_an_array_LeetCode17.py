class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = []
        for word_comp in words:
            for word in words:
                if word in word_comp and word != word_comp:
                    if word in ans:
                        continue
                    ans.append(word)
        return ans