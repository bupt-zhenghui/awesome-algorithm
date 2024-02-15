"""
对于矩阵matrix: 使用 m = len(matrix)语句获取矩阵的行
使用 n = len(matrix[0])语句获取矩阵的列
使用额外数组 row, col 来标记需要置零的行和列，空间复杂度为 O(mn)
"""
class Solution:
    def setZeroes(self, matrix) -> None:
        # m = len(matrix)
        # n = len(matrix[0])
        # row,col = [False]*m, [False]*n
        # for i in range(m):
        #     for j in range(n):
        #         if matrix[i][j] == 0:
        #             col[j] = True
        #             row[i] = True
        #
        # for i in range(m):
        #     for j in range(n):
        #         if row[i] or col[j]:
        #             matrix[i][j] = 0
        # return matrix
        m = len(matrix)
        n = len(matrix[0])
        flag_col = any(matrix[i][0] == 0 for i in range(m))
        flag_row = any(matrix[0][j] == 0 for j in range(n))
#         使用两个额外变量来存储，判断第1行，第1列是否含有0
#         接下来用矩阵的第一行和第一列来充当 法1中的标记数组
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0

        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if flag_col:
            for i in range(m):
                matrix[i][0] = 0

        if flag_row:
            for j in range(n):
                matrix[0][j] = 0

        return matrix
# 该方法所需的空间复杂度为 O(1)


print(Solution().setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))
