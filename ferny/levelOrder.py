# leetcode 102 二叉树的层序遍历
from utils import tree


class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        li = [root]
        ans = [[root.val]]
        while li:
            new_li = []
            for node in li:
                if node.left:
                    new_li.append(node.left)
                if node.right:
                    new_li.append(node.right)
            level_val = []
            for node in new_li:
                level_val.append(node.val)
            if level_val:
                ans.append(level_val)
            li = new_li
        return ans


root = tree.init_binary_tree([])
print(Solution().levelOrder(root))
