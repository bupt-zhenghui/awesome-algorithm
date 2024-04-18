class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

root = TreeNode(1)
a = TreeNode(2)
b = TreeNode(3)
c = TreeNode(4)
d = TreeNode(5)
root.left = a
root.right = b
a.left = c
a.right = d

class Solution:
    def diameterOfBinaryTree(self, root) -> int:
        self.length = 0

        def recur(root):
            if not root:
                return 0
            left = recur(root.left)
            right = recur(root.right)
            self.length = max(self.length, left + right)
            return max(left, right) + 1

        recur(root)
        return self.length

print(Solution().diameterOfBinaryTree(root))