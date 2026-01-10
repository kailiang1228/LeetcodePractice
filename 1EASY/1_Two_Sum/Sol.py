class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        prev = {}

        for i, num in enumerate(nums):
            last = target - num

            if last in prev:
                return [prev[last], i]

            prev[num] = i