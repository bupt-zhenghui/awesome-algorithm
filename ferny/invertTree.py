"""
226. 翻转二叉树/ 递归
"""
from utils.arrayToBitree import arrayToBitree
from utils.arrayToBitree import preOrder
from utils.arrayToBitree import inOrder
class Solution:
    def invertTree(self, root):
        if not root: return
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

root = arrayToBitree([4,2,7,1,3,6,9])
root1 = Solution().invertTree(root)
preOrder(root1)
print("-------------")
inOrder(root1)