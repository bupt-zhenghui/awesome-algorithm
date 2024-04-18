# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

arr = [1,2,3,4,5]
head = ListNode(arr[0])
tail = head
for num in arr[1:]:
    node = ListNode(num)
    tail.next = node
    tail = tail.next

class Solution:
    def reverseList(self, head):
        if not head or not head.next:
            return head
        pre = None
        cur = head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre


node = Solution().reverseList(head)
while node:
    print(node.val)
    node = node.next