class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head):
        # idx = 0
        new_set = set()
        while head:
            if head.next not in new_set:
                new_set.add(head)
                head = head.next
            else:
                return head.next
        return
