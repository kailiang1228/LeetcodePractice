class Solution(object):
    """Reverse bits of a given 32 bits signed integer."""
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 將整數轉為二進位字串，並補齊 32 位 (用 zfill)
        # zfill(width) 會在字串左邊補 0，直到字串長度達到 width
        # bin(n) 會得到 '0b101...'，所以要切掉前兩碼
        binary_str = bin(n)[2:].zfill(32)

        # 字串反轉
        # [::-1] 代表從頭到尾以 -1 步長反轉字串
        # [::1] 代表從頭到尾以 1 步長取得字串 (不反轉)
        # 反轉字串的另一種寫法: ''.join(reversed(binary_str))
        reversed_str = binary_str[::-1]

        # 將反轉後的二進位字串轉回 10 進位
        # int(x, 2) 會將 x 視為二進位字串並轉回整數
        return int(reversed_str, 2)


# 模擬測試
if __name__ == "__main__":
    s = Solution()
    nums = [43261596, 2147483644]

    for num in nums:
        print(s.reverseBits(num))

# 964176192, 1073741822
