"""
48. 旋转图像，先上下翻转，然后沿对角线翻转
"""
class Solution:
    def rotate(self, matrix) -> None:
        n = len(matrix)
        i,j = 0,n-1
        while i <= j:
            matrix[i],matrix[j] = matrix[j],matrix[i]
            i += 1
            j -= 1
#         先上下翻转，然后沿主对角线翻转
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        return matrix


print(Solution().rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))
