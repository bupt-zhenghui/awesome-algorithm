"""
104. 二叉树的最大深度.深度优先搜索，递归
"""
from utils.arrayToBitree import arrayToBitree
class Solution:
    def maxDepth(self, root) -> int:
        if not root: return 0
        ldepth = self.maxDepth(root.left)
        rdepth = self.maxDepth(root.right)
        maxdepth = max(ldepth,rdepth) + 1
        return maxdepth

root = arrayToBitree([1,None,2])
print(Solution().maxDepth(root))

