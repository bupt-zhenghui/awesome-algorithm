"""
108. 将有序数组转为二叉搜索树
二叉搜索树的中序遍历 一定为升序序列
二叉搜索树的左子树若存在，其所有节点的值均小于根节点的值
二叉搜索树的右子树若存在，其所有节点的值均大于根节点的值
递归终止条件是 left > right
中序遍历，总是选择中间位置左边的数字作为根节点。则 mid = (left+right)//2.其中，left,right为下标
"""
from utils.arrayToBitree import preOrder
from utils.arrayToBitree import inOrder
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums):
        def bst(l,r):
            if l > r: return
            mid = (l+r) // 2
            root = TreeNode(nums[mid])
            root.left = bst(l,mid-1)
            root.right = bst(mid+1,r)
            return root
        l,r = 0, len(nums)-1
        root = bst(l,r)
        return root

root = Solution().sortedArrayToBST([10,-3,0,5,9])
preOrder(root)
print("------------")
inOrder(root)

