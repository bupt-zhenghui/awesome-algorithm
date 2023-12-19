# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def hasCycle(self, head):
        new_set = set()
        p = head
        if not p:
            return False
        new_set.add(p)
        while p:
            p = p.next
            if p in new_set:
                return True
            else:
                new_set.add(p)
        return False


