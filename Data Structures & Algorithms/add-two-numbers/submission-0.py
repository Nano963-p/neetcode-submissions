# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        tmp = ListNode(0)
        curr = tmp
        reste = 0

        while l1 or l2 or reste != 0:
            val1 = 0
            val2 = 0

            if l1:
                val1 = l1.val
                l1 = l1.next

            if l2:
                val2 = l2.val
                l2 = l2.next

            sum = val1 + val2 + reste

            curr.next = ListNode(sum % 10)
            curr = curr.next

            reste = sum // 10

        return tmp.next   