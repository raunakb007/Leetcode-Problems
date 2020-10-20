class Solution:

    def search(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            m = (left+right)//2
            if nums[m]>target:
                right = m-1
            elif nums[m]<target:
                left = m+1
            if nums[m] == target:
                return m
        else:
            return -1
