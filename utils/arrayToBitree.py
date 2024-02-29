class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# 层次遍历，构造二叉树
def arrayToBitree(arr):
    if not arr: return
    root = TreeNode(arr[0])
    node_list = [root]
    i = 1
    while node_list:
        node_list_new = []
        for node in node_list:
            if i == len(arr): break
            if arr[i] is not None:
                new_node = TreeNode(arr[i])
                node.left = new_node
                node_list_new.append(node.left)
            i = i + 1
            if i == len(arr): break
            if arr[i] is not None:
                new_node = TreeNode(arr[i])
                node.right = new_node
                node_list_new.append(node.right)
            i = i + 1
            if i == len(arr): break
        node_list = node_list_new
    return root

def preOrder(root):
    if not root: return
    print(root.val)
    preOrder(root.left)
    preOrder(root.right)

def inOrder(root):
    if not root: return
    inOrder(root.left)
    print(root.val)
    inOrder(root.right)

def postOrder(root):
    if not root: return
    postOrder(root.left)
    postOrder(root.right)
    print(root.val)


# root = arrayToBitree([4,2,7,1,3,6,9])
# preOrder(root)
# print("-----------------")
# inOrder(root)
# print("------------------")
# postOrder(root)