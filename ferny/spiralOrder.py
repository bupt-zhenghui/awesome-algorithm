import numpy as np
class Solution:
    def spiralOrder(self, matrix):
        ans = []
        while matrix:
            m = len(matrix)
            n = len(matrix[0])
            for j in range(n):
                ans.append(matrix[0][j])
            for i in range(1,m):
                ans.append(matrix[i][n-1])
            if m >= 2:
                for p in range(n-2,0,-1):
                    ans.append(matrix[m-1][p])
            if n >= 2:
                for q in range(m-1,0,-1):
                    ans.append(matrix[q][0])
            matrix0 = matrix[1:m-1]
            new_matrix = [row[1:n-1] for row in matrix0]
            # 注意学习如何截取矩阵的一部分
            if new_matrix:
                if new_matrix[0]:
                    matrix = new_matrix
                else:
                    break
            else:
                break
        return ans


print(Solution().spiralOrder([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]]))