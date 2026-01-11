# class Solution(object):
#     def isPalindrome(self, x):
#         """
#         :type x: int
#         :rtype: bool
#         """
#         s = str(x)
#         pos = [0] * len(s)
#         neg = [0] * len(s)
#         site = len(s)
#         k = 0

#         for i, num in enumerate(s):
#             pos[i] += num
#             site -= 1
#             neg[site] = num

#         for i in range(len(s)):
#             if pos[i] == neg[i]:
#                 k += 1
            
#         if k == len(s):
#             return True
#         else:
#             return False 

#雙指針
class Solution(object):
    """Determine whether an integer is a palindrome. Reads the same backward as forward."""
    def isPalindrome(self, x):
        s = str(x)
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

# 模擬測試
if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        (121, True),
        (-121, False),
        (10, False),
        (12321, True)
    ]

    for x, expected in test_cases:
        final = sol.isPalindrome(x)
        print(f"Input: {x} | Expected: {expected} | Actual: {final}")

# True, False, False, True
