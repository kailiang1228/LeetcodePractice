class Solution(object):
    """Reverse bits of a given 32 bits signed integer."""
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0

        # 逐位反轉(32位元)
        for i in range(32):
            # 取得 n 的最右邊一位
            # & 1 會得到該位元是 0 還是 1
            bit = n & 1
            # 將該位元加入結果的最左邊
            # | 1 將該位元設為 1，<< 1 將結果左移一位
            result = (result << 1) | bit
            # n 右移一位，準備處理下一位
            n >>= 1

        return result

# 模擬測試
if __name__ == "__main__":
    s = Solution()
    nums = [43261596, 2147483644]

    for num in nums:
        print(s.reverseBits(num))

# 964176192, 1073741822
