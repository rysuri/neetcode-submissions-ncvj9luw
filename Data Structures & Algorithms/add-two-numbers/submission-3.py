# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # My first thoughts, this seems like a very straight forward problem.
        # Loop through the first list, then the second. While looping through, keep a sum.
        # The sum should be added with powers of 10. For example the first element should be
        # 1 * 10^0. next 2* 10^1, then add.

        total = 0

        curr = l1
        power = 0

        while curr:
            digit = curr.val * (10**power)
            print(digit)
            total = total + digit
            power += 1
            curr = curr.next

        print(total)
        curr = l2
        power = 0

        while curr:
            digit = curr.val * (10**power)
            total = total + digit
            power += 1
            curr = curr.next
        print(total)

        resultPointer = None
        curr = resultPointer
        if total == 0:
            return ListNode(0)

        while total > 0:
            digit = total % 10
            print(digit)

            newNode = ListNode(digit)

            if resultPointer == None:
                resultPointer = newNode
                curr = resultPointer
            else:
                curr.next = newNode
                curr = newNode

            total = total // 10


        print(total)
        return resultPointer