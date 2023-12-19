# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from ferny import arrayToLinklist

class Solution:
    def mergeTwoLists(self, list1, list2):

        def insert(cur1,cur2):
            while cur1.next:
                if cur1.val <= cur2.val <= cur1.next.val:
                    tmp = cur2.next
                    cur2 = cur1.next
                    cur2.next = cur1.next
                    cur1 = cur2

                    cur2 = tmp
                else:
                    cur1 = cur1.next
            cur1.next = cur2

        if not list1:
            return list2
        if not list2:
            return list1

        if list1.val <= list2.val:
            cur1 = list1
            cur2 = list2
            insert(cur1,cur2)
            return list1
        else:
            cur1 = list2
            cur2 = list1
            insert(cur1,cur2)
            return list2

l1 = Solution().arrayToLinklist([1,2,4])
l2 = arrayToLinklist([1,3,4])

print(Solution().mergeTwoLists([1,2,4],[1,3,4]))

