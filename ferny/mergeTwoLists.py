# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# from ferny.arrayToLinklist import arrayTolinklist
#
#
# class Solution:
#     def mergeTwoLists(self, list1, list2):
#
#         def insert(cur1, cur2):
#             while cur1 and cur2:
#                 if cur1.next:
#                     if cur1.val <= cur2.val <= cur1.next.val:
#                         tmp1 = cur1.next
#                         tmp2 = cur2.next
#                         cur1.next = cur2
#                         cur2.next = tmp1
#                         cur1 = cur2
#
#                         cur2 = tmp2
#                     else:
#                         cur1 = cur1.next
#                 else:
#                     cur1.next = cur2
#                     return
#
#         if not list1:
#             return list2
#         if not list2:
#             return list1
#
#         if list1.val <= list2.val:
#             cur1 = list1
#             cur2 = list2
#             insert(cur1, cur2)
#             return list1
#         else:
#             cur1 = list2
#             cur2 = list1
#             insert(cur1, cur2)
#             return list2
#
#
# list1 = arrayTolinklist([-9,3])
# list2 = arrayTolinklist([5,7])
#
# print(Solution().mergeTwoLists(list1, list2))
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        if not list1: return list2
        if not list2: return list1
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next,list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1,list2.next)
            return list2