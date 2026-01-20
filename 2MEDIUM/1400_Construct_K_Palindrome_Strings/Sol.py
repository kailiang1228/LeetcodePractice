class Solution(object):
    def canConstruct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        

# 模擬測試
if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        ([2, 2, 1], 1),
        ([4, 1, 2, 1, 2], 4),
        ([1], 1)
    ]

    for nums, expected in test_cases:
        final = sol.canConstruct(nums)
        print(f"Input: {nums} | Expected: {expected} | Actual: {final}")

# 1, 4, 1
