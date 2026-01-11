# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        #虛擬頭節點 (方便返回結果) 神器
        dummy_head = ListNode(0)
        current = dummy_head # 當前節點
        carry = 0 # 進位

        # 當 l1 或 l2 有節點，或有進位時繼續迴圈
        while l1 is not None or l2 is not None or carry != 0: # 只要有一個條件成立就繼續
            val1 = l1.val if l1 is not None else 0 # 取得 l1 當前節點的值，若為 None 則為 0
            val2 = l2.val if l2 is not None else 0 # 取得 l2 當前節點的值，若為 None 則為 0

            # 計算當前位的和及進位
            total = val1 + val2 + carry 
            carry = total // 10 # 整除10 十位
            new_digit = total % 10 # 取餘數10 個位

            # 創建新節點並連接到結果鏈表
            current.next = ListNode(new_digit) # 新節點
            current = current.next # 移動當前節點到新節點 進位

            # 移動到下一個節點
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

        return dummy_head.next # 返回結果鏈表的頭節點 (跳過虛擬頭節點)

# 模擬測試
if __name__ == "__main__":
    sol = Solution()

    # Helper function to create a linked list from a list
    def create_linked_list(lst):
        dummy_head = ListNode(0)
        current = dummy_head
        for number in lst:
            current.next = ListNode(number)
            current = current.next
        return dummy_head.next

    # Helper function to print linked list
    def print_linked_list(node):
        values = []
        while node:
            values.append(str(node.val))
            node = node.next
        print(" -> ".join(values))

    # Test cases
    l1 = create_linked_list([2, 4, 3])
    l2 = create_linked_list([5, 6, 4])
    result = sol.addTwoNumbers(l1, l2)
    print_linked_list(result)  # Expected Output: 7 -> 0 -> 8

    l1 = create_linked_list([0])
    l2 = create_linked_list([0])
    result = sol.addTwoNumbers(l1, l2)
    print_linked_list(result)  # Expected Output: 0

    l1 = create_linked_list([9, 9, 9, 9, 9, 9, 9])
    l2 = create_linked_list([9, 9, 9, 9])
    result = sol.addTwoNumbers(l1, l2)
    print_linked_list(result)  # Expected Output: 8 -> 9 -> 9 -> 9 -> 0 -> 0 -> 0 -> 1

# 7 -> 0 -> 8
