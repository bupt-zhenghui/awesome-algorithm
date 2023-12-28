class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


def arrayToLinklist_new(arr):
    if not arr: return
    first = arr[0]
    head = Node(first[0])
    tail = head
    dic = {0: head}
    for i, tul in enumerate(arr[1:]):
        node = Node(tul[0])
        tail.next = node
        tail = node
        dic[i + 1] = tail
    i = 0
    tail = head
    while tail:
        num = arr[i]
        if num[1] is None:
            tail.random = None
        else:
            tail.random = dic[num[1]]
        tail = tail.next
        i = i + 1
    return head

head = arrayToLinklist_new([[7,None],[13,0],[11,4],[10,2],[1,0]])
