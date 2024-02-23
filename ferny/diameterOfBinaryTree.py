"543. 二叉树的直径"
from utils.arrayToBitree import arrayToBitree
class Solution:
    def diameterOfBinaryTree(self, root):
        self.ans = 1

        def depth(root):
            if not root: return 0
            left = depth(root.left)
            right = depth(root.right)
            self.ans = max(self.ans, left + right + 1)
            return max(left, right) + 1

        depth(root)
        return self.ans - 1


root = arrayToBitree([1,2,3,4,5])
print(Solution().diameterOfBinaryTree(root))