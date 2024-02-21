"""
240. 搜索二维矩阵：
1. 对每一行使用二分查找: O(mlogn)
2. Z字形查找 0(m+n)
以(0,n-1)为(x,y)的起始位置，希望搜索范围在以 (x,y)为右上角的范围内。如果 target > matrix[x][y]: x += 1
否则: y -= 1
3. 直接查找 0(mn)
"""
class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        # for i in range(m):
        #     p,q = 0, n-1
        #     while p <= q:
        #         mid = (p + q) // 2
        #         if matrix[i][mid] == target:
        #             return True
        #         elif matrix[i][mid] > target:
        #             q = mid - 1
        #         else:
        #             p = mid + 1
        # return False
        x, y = 0, n-1
        while x < m and y > -1:
            if matrix[x][y] == target:
                return True
            elif matrix[x][y] < target:
                x += 1
            else:
                y -= 1
        return False


print(Solution().searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],5))