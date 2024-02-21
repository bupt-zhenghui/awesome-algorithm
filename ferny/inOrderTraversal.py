from utils.arrayToBitree import arrayToBitree
class Solution:
    def inorderTraversal(self, root):
        if not root: return []
        ans = self.inorderTraversal(root.left)
        ans = ans + [root.val]
        ans = ans + self.inorderTraversal(root.right)
        return ans


root = arrayToBitree([1,2,3,4])
print(Solution().inorderTraversal(root))
"""

94. 二叉树的中序遍历，并返回数组结果
"""