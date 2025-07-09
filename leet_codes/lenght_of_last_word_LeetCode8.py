class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        for word in s:
            if word == ' ':
                continue
            else:
                list_words = [elements for elements in s.lower().split()]
        for word in range(len(list_words)):
            if word == len(list_words)-1:
                last_word = list_words[word]
        return len(last_word)
            