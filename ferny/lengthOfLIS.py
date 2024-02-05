class Solution:
    def lengthOfLIS(self, nums) -> int:
        dp = [1]*len(nums)
        for i in range(1,len(nums)):
            arr = []
            j = i - 1
            while j >= 0:
                if nums[i] > nums[j]:
                    arr.append(dp[j]+1)
                j = j - 1
            if arr:
                dp[i] = max(arr)

        return max(dp)

"""
300. 最长递增子序列
dp[i] 表示到 i 为截止的最长递增子序列的长度
遍历 j < i；当遇到一个比 num[i]小的值时，arr数组中就加上 dp[j] + 1。
取arr数组中的最大值 即为 dp[i]
最后返回数组中的最大值即可。
"""
print(Solution().lengthOfLIS([7,7,7,7,7,7,7]))
