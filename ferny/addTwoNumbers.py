# Definition for singly-linked list.
from utils.arrayToLinklist import arrayTolinklist
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        list1, list2 = [],[]
        while l1:
            list1.append(l1.val)
            l1 = l1.next
        while l2:
            list2.append(l2.val)
            l2 = l2.next
        list1.reverse()
        list2.reverse()
        n1 = len(list1)
        n2 = len(list2)
        total1, total2 = 0, 0
        for i, num in enumerate(list1):
           total1 = total1 + num*pow(10,n1-i-1)
        for j, num in enumerate(list2):
            total2 = total2 + num * pow(10,n2-j-1)
        total = total2 + total1
        print(total)

        if total == 0:
            return ListNode(0)
        list3 = []
        while total > 0:
            r = total // 10
            list3.append(total - r*10)
            total = r
        # print(list3)

        head = ListNode(list3[0])
        tail = head
        for num in list3[1:]:
            node = ListNode(num)
            tail.next = node
            tail = tail.next

        return head

l1 = arrayTolinklist([0])
l2 = arrayTolinklist([0])
print(Solution().addTwoNumbers(l1,l2).val)


