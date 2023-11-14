"""
Leetcode 543. 二叉树的直径
url: https://leetcode.cn/problems/diameter-of-binary-tree/
"""
from utils.tree import init_binary_tree


class Solution:
    def diameterOfBinaryTree(self, root) -> int:
        self.ans = 0

        def dfs(node):
            if not node: return 0
            left = dfs(node.left)
            right = dfs(node.right)
            self.ans = max(self.ans, left + right + 1)
            return max(left, right) + 1

        dfs(root)
        return self.ans - 1


if __name__ == '__main__':
    root = init_binary_tree([1, 2, 3, 4, 5])
    ans = Solution().diameterOfBinaryTree(root)
    print(ans)
