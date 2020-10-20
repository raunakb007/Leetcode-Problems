class Solution:

    def addToArrayForm(self, A, K):
        res = []
        s = str(int("".join([str(i) for i in A])) + K)
        print(s)
        for ch in s:
            res.append(int(ch))
        return res
