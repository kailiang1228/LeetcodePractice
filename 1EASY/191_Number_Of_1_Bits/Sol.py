class Solution(object):
    """Count bits."""
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n > 0:
            #最後為1
            if n & 1: #不用==1 if 預設=1 觸發
                count += 1
            #右移一位
            n >>= 1

        return count


# 模擬測試
if __name__ == "__main__":
    s = Solution()
    nums = [11, 128, 2147483645]

    for num in nums:
        print(s.hammingWeight(num))
    # print(s.hammingWeight(11)) # 看看輸出是不是 3 (二進位 1011 有三個1)
    # print(s.hammingWeight(128))
    # print(s.hammingWeight(2147483645))
