class Solution:
    def coinChange(self, coins, amount):
        if amount == 0: return 0
        dp = [0]*(amount+1)
        dp[0] = 0
        sorted(coins)
        if coins[0] == 1: dp[1] = 1
        else: dp[1] = -1
        i = 2
        while i <= amount:
            arr = []
            for c in coins:
                if i - c >= 0 and dp[i-c] != -1:
                    arr.append(dp[i-c])
            if not arr: dp[i] = -1
            else: dp[i] = min(arr) + 1
            i = i + 1
        return dp[-1]

"""
322. 零钱兑换
注意状态转移方程：
假设 值为 i 的金额所需的最小兑换个数为 f[i]。则当 c 属于 coins是，有状态转移方程
f[i] = f[i-c] + 1
最后遍历所有coin中的c，找到 f[i-c]的最小值即可
注意细节的处理：当金额 i-c 不能被硬币兑换时，f[i-c] = -1; 此时对应的 f[i]不能被 f[i-c]的金额+1 兑换
"""
print(Solution().coinChange([2,4],10))