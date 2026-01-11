class Solution(object):
    """Given a non-empty array of integers, Find that single one."""
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

# 模擬測試
if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1])
    ]

    for nums, target, expected in test_cases:
        final = sol.twoSum(nums, target)
        print(f"Input: nums={nums}, target={target} | Expected: {expected} | Actual: {final}")

# [0, 1], [1, 2], [0, 1]
