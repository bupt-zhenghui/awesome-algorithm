def maxsubarray(nums):
    if not nums:
        return "invalid"
    n = len(nums)
    if n == 1:
        return nums[0]
    dp = [0]*n
    dp[0] = nums[0]
    for i in range(1,n):
        if dp[i-1] + nums[i] >= nums[i]:
            dp[i] = dp[i-1] + nums[i]
        else:
            dp[i] = nums[i]
    return max(dp)


nums = [1]
print(maxsubarray(nums))