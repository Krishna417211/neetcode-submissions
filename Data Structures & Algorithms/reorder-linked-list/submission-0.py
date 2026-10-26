# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        dummy = ListNode(0)
        current = dummy

        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        curr = slow.next
        slow.next = None

        while curr:
            curr.next, prev, curr = prev, curr, curr.next


        while head and prev:
            temp1 = head.next
            temp2 = prev.next


            head.next = prev
            prev.next = temp1

            head = temp1
            prev = temp2

        