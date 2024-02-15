class Solution:
    def setZeroes(self, matrix) -> None:
        m = len(matrix)
        n = len(matrix[0])
        row,col = [False]*m, [False]*n
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    col[j] = True
                    row[i] = True

        for i in range(m):
            for j in range(n):
                if row[i] or col[j]:
                    matrix[i][j] = 0
        return matrix

"""
对于矩阵matrix: 使用 m = len(matrix)语句获取矩阵的行
使用 n = len(matrix[0])语句获取矩阵的列
使用额外数组 row, col 来标记需要置零的行和列，空间复杂度为 O(mn)
"""


print(Solution().setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))
