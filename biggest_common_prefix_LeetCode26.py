class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        m = len(strs)
        sorted_strs = sorted(strs)
        first = sorted_strs[0]
        last = sorted_strs[m-1]
        for i in range(len(first)):
            if i in range(len(last)):
                if first[i] == last[i]:
                    result += first[i]
                else:
                    return result
        return result