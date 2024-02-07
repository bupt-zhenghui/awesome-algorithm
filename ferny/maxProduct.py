class Solution:
    def maxProduct(self, nums) -> int:
        if len(nums) == 1: return nums[0]
        dp_max = [0]*len(nums)
        dp_min = [0]*len(nums)
        dp_max[0] = max(0,nums[0])
        dp_min[0] = min(0,nums[0])
        for i in range(1,len(nums)):
            dp_max[i] = max(dp_max[i-1]*nums[i],dp_min[i-1]*nums[i],nums[i])
            dp_min[i] = min(dp_max[i-1]*nums[i],dp_min[i-1]*nums[i],nums[i])
        return max(dp_max)



print(Solution().maxProduct([-2]))
"""
dp_max[i]表示以 i 为终止的数组对应的 正 的最大值
dp_min[i]表示以 i 为终止的数组对应的 负 的最小值
维护两个数组，以及 max,min函数的运用可以不适用 if else语句判断，否则情况总写不全，而且越来越乱
与最长连续子数组的和思想一致
"""