class Solution:

    def uncommonFromSentences(self, A, B):
        word_count = {}
        for word in A.split():
            word_count[word] = word_count.get(word, 0) + 1
        for word in B.split():
            word_count[word] = word_count.get(word, 0) + 1
        return [word for word in word_count if word_count[word] == 1]
