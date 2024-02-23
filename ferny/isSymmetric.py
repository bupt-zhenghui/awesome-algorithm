from collections import deque

from utils.arrayToBitree import arrayToBitree
class Solution:
    def isSymmetric(self, root):
        if (not root.left and root.right) or (not root.right and root.left): return False
        node_list = [root]
        while node_list:
            ans = []
            new_list = []
            for node in node_list:
                if node.left:
                    new_list.append(node.left)
                    ans.append(node.left.val)
                else:
                    ans.append(-101)
                if node.right:
                    new_list.append(node.right)
                    ans.append(node.right.val)
                else:
                    ans.append(-101)
            if ans != ans[::-1]: return False
            node_list = new_list
        return True


root = arrayToBitree([1,2,2,None,3,None,3])
print(Solution().isSymmetric(root))

