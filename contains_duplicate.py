class Solution:

    def containsDuplicate(self, nums):
        d = {}
        for n in nums:
            if d.get(n, None) is None:
                d[n] = True
            else:
                return True
        return False
