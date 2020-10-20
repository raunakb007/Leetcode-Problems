class Solution:

    def findTheDifference(self, s, t):
        sum_s, sum_t = 0, 0

        for i in range(len(t)):

            if i == len(t)-1:
                sum_t += ord(t[i])
            else:
                sum_s += ord(s[i])
                sum_t += ord(t[i])

        return chr(sum_t-sum_s)
