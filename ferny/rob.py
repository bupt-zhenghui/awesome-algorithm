class Solution:
    def rob(self, nums):
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums[0],nums[1])
        dp = [0]*len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        for k in range(2,len(nums)):
            dp[k] = max(dp[k-2]+nums[k],dp[k-1])
        return dp[-1]
#         动态规划：
# 若偷第 k+1 所房子，则所偷金额的最大值 = 前 k-1 所房子的最大金额 dp[k-2] + 第 k + 1所房子的金额 nums[k]
# 若不偷第 k+1 所房子，则所偷金额的最大值 = 前 k 所房子的最大金额 dp[k-1]

print(Solution().rob([2,1,1,2]))
