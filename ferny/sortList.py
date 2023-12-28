# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head):
        if not head or not head.next: return head
        arr = []
        while head:
            arr.append(head.val)
            head = head.next

        arr.sort()
        head = ListNode(arr[0])
        tail = head
        for num in arr[1:]:
            node = ListNode(num)
            tail.next = node
            tail = tail.next
        return head


