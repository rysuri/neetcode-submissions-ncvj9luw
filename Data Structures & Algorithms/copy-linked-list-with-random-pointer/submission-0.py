"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        # What I am thinking is a 2 pass algorithm.
        # In sync, we will have 2 pointers, one pointing to the original, one to the copy.
        # The first pass will create the nodes, using the next pointers, keeping 'random' null.
        # 

        oldToCopy = {None : None}

        curr = head
        while curr:
            # create copy.
            copy = Node(curr.val)
            oldToCopy[curr] = copy
            curr = curr.next

        # second pass

        curr = head
        while curr:
            copy = oldToCopy[curr]
            copy.next = oldToCopy[curr.next]

            copy.random = oldToCopy[curr.random]
            curr= curr.next
        
        return oldToCopy[head]

        