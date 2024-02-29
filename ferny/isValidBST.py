from utils.arrayToBitree import arrayToBitree

class Solution:
    def isValidBST(self, root) -> bool:
        def helper(root,lower,upper):
            if not root: return True

            val = root.val
            if not val > lower or not val < upper:
                return False

            f1 = helper(root.left,lower,root.val)
            if not f1: return False
            f2 = helper(root.right,root.val,upper)
            if not f2: return False
            return True
        return helper(root,float('-inf'),float('inf'))

root = arrayToBitree([2,1,3])
print(Solution().isValidBST(root))