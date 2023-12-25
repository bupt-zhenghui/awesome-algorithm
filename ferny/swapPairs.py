from ferny.arrayToLinklist import arrayTolinklist
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:

    def bianli(self, head):
        if not head: return
        while head:
            print(head.val)
            head = head.next

    def swapPairs(self, head):
        if not head: return []
        if not head.next: return head
        pre = ListNode(-1)
        cur = head
        ans = head.next
        while cur:
            post = cur.next
            if not post:
                return ans
            tmp = post.next
            post.next = cur
            pre.next = post
            cur.next = tmp

            pre = cur
            cur = cur.next

        self.bianli(ans)
        return ans


head = arrayTolinklist([1,2,3,4,5,6])
tou = Solution().swapPairs(head)

