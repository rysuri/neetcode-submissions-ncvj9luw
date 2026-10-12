# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        curr = head
        length = 0

        while curr != None:
            curr = curr.next
            length = length + 1


        temp = length - n

        if temp == 0:
            return head.next

        curr = head
        for i in range(temp-1):
            curr = curr.next
        
        curr.next = curr.next.next

        return head

