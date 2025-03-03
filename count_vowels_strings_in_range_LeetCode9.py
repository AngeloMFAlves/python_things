class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        index_prefix = 0
        prefix = []
        vowels = ['a','e','i','o','u']
        ans_list = []
        for word in words:
            if word[0] in vowels and word[len(word)-1] in vowels:
                index_prefix += 1
                prefix.append(index_prefix)
            else:
                prefix.append(index_prefix)
        for index in queries:
            ans = 0
            start, end = index[0],index[1]
            if start == 0:
                ans = prefix[end]
            else:
                ans = prefix[end] - prefix[start-1]
            ans_list.append(ans)
        return(ans_list)