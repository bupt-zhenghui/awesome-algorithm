# The official implementation of Binary Tree Node
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# 前缀树
class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = dict()


def init_binary_tree(array):
    if not array: return None
    root = TreeNode(array[0])
    node_list = [root]
    idx = 1
    while node_list:
        new_list = []
        for node in node_list:
            if idx == len(array): break
            node.left = TreeNode(array[idx]) if array[idx] is not None else None
            if node.left: new_list.append(node.left)
            idx += 1
            if idx == len(array): break
            node.right = TreeNode(array[idx]) if array[idx] is not None else None
            if node.right: new_list.append(node.right)
            idx += 1
        if idx == len(array): break
        node_list = new_list
    return root


def pre_order(node):
    if not node: return
    print(node.val)
    pre_order(node.left)
    pre_order(node.right)


def in_order(node):
    # TODO
    pass


def post_order(node):
    # TODO
    pass


def hierarchical_traversal(node):
    # TODO
    pass
