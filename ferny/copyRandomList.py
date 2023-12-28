from ferny.arrayToLinklist_new import arrayToLinklist_new

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head):
        if not head: return
        new_head = Node(head.val)
        new_tail = new_head
        tail = head.next
        while tail:
            node = Node(tail.val)
            new_tail.next = node
            new_tail = node
            tail = tail.next
        # 构建只关心next的新链表
        dic = {}
        i = 0
        tail = head
        while tail:
            dic[tail] = i
            i = i + 1
            tail = tail.next

        new_dic = {}
        j = 0
        new_tail = new_head
        while new_tail:
            new_dic[j] = new_tail
            j = j + 1
            new_tail = new_tail.next

        new_tail = new_head
        while head:
            if head.random in dic:
                val = dic[head.random]
                new_tail.random = new_dic[val]
            else:
                new_tail.random = None
            head = head.next
            new_tail = new_tail.next
        # 找出head.random指向的位置，然后对应 new_head.random指向的位置

        return new_head

head = arrayToLinklist_new([[7,None],[13,0],[11,4],[10,2],[1,0]])
print(Solution().copyRandomList(head))
