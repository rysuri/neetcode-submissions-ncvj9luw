# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()   # placeholder so prev is never None
        prev = dummy

        curser1 = list1
        curser2 = list2

        while curser1 and curser2:
            if curser1.val <= curser2.val:   # <= covers the equal case too
                prev.next = curser1
                curser1 = curser1.next
            else:
                prev.next = curser2
                curser2 = curser2.next
            prev = prev.next

        # One list is used up; the other is already linked, so attach it in one step
        prev.next = curser1 if curser1 else curser2

        return dummy.next