class Solution:
    def canPartition(self, nums) -> bool:
        """
        0-1背包问题（是否选取该值）
        对列表进行初始化
        dp[i][j]  = True 表示从数组的序号为 i （包含i）个数中任选k个数（k可以为0）,使其和为 j
        则 当 j >= nums[i] 时，此时若选取 nums[i]，则 dp[i][j] = dp[i-1][j-nums[i]]
                                若不选取 nums[i], 则 dp[i][j] = dp[i-1][j]
                                注意：二者只要有一个为 True, dp[i][j]即为True
        当 j < nums[i]时，此时有 dp[i][j] = dp[i-1][j]
        """
        n = len(nums)
        if len(nums) == 1: return False
        totol = sum(nums)
        if totol/2 != totol // 2: return False
        # 总和为奇数的话不能被分为2组
        if max(nums) > totol/2: return False
        # 数组中的最大值大于总和的一半，也不能被分为2组
        target = totol//2
        # 使用列表表达式创建一个 n 行 target + 1列的列表
        cols = target + 1
        rows = n
        dp = [[False] * cols for _ in range(rows)]

        # 首先进行初始化
        for m in range(n):
            dp[m][0] = True
        dp[0][nums[0]] = True

        for i in range(n):
            for j in range(target+1):
                if j < nums[i]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j-nums[i]] or dp[i-1][j]
#       j 的值 从 0 到 target（目标是总和的一半）为止

        return dp[n-1][target]

print(Solution().canPartition([1,2,3,4]))

"""
需要额外学习如何创建 m 行 n 列的数组
col = n
row = m
dp = [[0]*col for _ in range(m)]
"""