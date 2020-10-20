class Solution:

    def nextGreatestLetter(self, letters, target):
        tar = ord(target)
        for l in letters:
            if ord(l) > tar:
                return l
        return letters[0]
