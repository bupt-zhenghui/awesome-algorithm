class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def arrayTolinklist(self, nums):
        if not nums:
            return
        if nums:
            # 采用尾插法
            head = ListNode(nums[0])
            tail = head
            for num in nums[1:]:
                linknode = ListNode(num)
                tail.next = linknode
                tail = tail.next
            return head

    def bianli(self,head):
        if not head:
            return
        while head:
            print(head.val)
            head = head.next

head = Solution().arrayTolinklist([1,2,3,4,5,7,9])
Solution().bianli(head)
