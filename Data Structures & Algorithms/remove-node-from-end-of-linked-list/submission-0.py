# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        tmp = ListNode(0)
        tmp.next = head

        slow = tmp
        fast = tmp

        i = 0

        while i < n + 1:
            fast = fast.next
            i += 1

        while fast is not None:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return tmp.next