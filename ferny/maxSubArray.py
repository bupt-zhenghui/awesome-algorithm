# 53. 最大子数组和
#    动态规划题
class Solution:
    def maxSubArray(self, nums):
        if len(nums) == 1:
            return nums[0]
        dp = []
        for idx, num in enumerate(nums):
            if idx == 0:
                dp.append(num)
            else:
                dp.append(max(dp[idx - 1] + num, num))

        # dp = [0]*len(nums)
        # 或者创建 dp 数组时要指定空间的大小
        # for idx, num in enumerate(nums):
        #     if idx == 0:
        #         dp[idx] = num
        #     else:
        #         dp[idx] = max(dp[idx-1]+num, num)
        # dp.sort()
        return dp[-1]




print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))




