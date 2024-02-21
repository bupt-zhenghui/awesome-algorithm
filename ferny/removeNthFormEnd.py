from utils.arrayToLinklist import arrayTolinklist
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head, n: int):
        idx = 1
        tmp = head
        while tmp.next:
            tmp = tmp.next
            idx = idx + 1
        print(idx)

        k = idx - n + 1
        j = 1
        cur = head
        if n == idx:
            return head.next
        while cur:
            if j == k - 1:
                t = cur.next
                post = t.next
                cur.next = post
                return head
            else:
                cur = cur.next
                j = j + 1




head = arrayTolinklist([1,2,3,4,5])
print(Solution().removeNthFromEnd(head,2))