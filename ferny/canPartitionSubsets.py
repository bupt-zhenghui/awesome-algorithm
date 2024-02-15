class Solution:
    def canPartitionKSubsets(self, nums, k: int) -> bool:
        total = sum(nums)
        if total % k != 0: return False
        if max(nums) > total // k: return False
        target = total // k
        row = len(nums)
        col = target + 1
        dp = [[False] * col for _ in range(row)]
        for i in range(row):
            dp[i][0] = True
        dp[0][nums[0]] = True
        for i in range(row):
            for j in range(col):
                if j < nums[i]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i]]
        return dp[row-1][target]

print(Solution().canPartitionKSubsets([2,2,2,2,3,4,5],4))