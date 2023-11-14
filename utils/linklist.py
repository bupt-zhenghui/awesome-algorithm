class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def init_link_list(array):
    root = ListNode(0)
    head = root
    for k in array:
        node = ListNode(k)
        head.next = node
        head = head.next
    return root.next


def traverse_link_list(node):
    # TODO
    pass
