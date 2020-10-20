class Solution:

    def twoSum(self, nums, target):
        lookup = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if lookup.get(diff, None) is not None and lookup.get(diff, None) != i:
                return [i, lookup.get(diff)]
            lookup[nums[i]] = i
