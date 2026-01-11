class Solution(object):
    """Given a non-empty array of integers, Find that single one."""
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0

        # 遍歷陣列中的每個數字
        for num in nums:
            # XOR 運算 (相同為0，不同為1)
            # 利用 XOR 的特性：a ^ a = 0 和 a ^ 0 = a
            # 將所有數字進行 XOR 運算，成對出現的數字會互相抵消，最後剩下的就是單獨出現的數字
            # 例如：如果陣列是 [4, 1, 2, 1, 2]
            # 運算過程為：0 ^ 4 ^ 1 ^ 2 ^ 1 ^ 2
            # 其中 1 和 2 會互相抵消，最後結果為 4
            result ^= num

        return result

# 模擬測試
if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        ([2, 2, 1], 1),
        ([4, 1, 2, 1, 2], 4),
        ([1], 1)
    ]

    for nums, expected in test_cases:
        final = sol.singleNumber(nums)
        print(f"Input: {nums} | Expected: {expected} | Actual: {final}")

# 1, 4, 1
