class Solution:
    def numSquares(self, n: int) -> int:
        if n == 1: return 1
        dp = [0]*(n+1)
        dp[0] = 0
        dp[1] = 1
        i = 2
        while i <= n:
            j = int(pow(i,0.5))
            seq = []
            while j >= 1:
                seq.append(dp[i-j*j])
                j -= 1
            tmp_cnt = min(seq)
            dp[i] = 1 + tmp_cnt
            i = i + 1
        return dp[-1]

'''
假设整数 i 可最少由 f(i) 个完全平方数表示
j 属于 [1, pow(i,1/2)]，对应的整数 i - j^2 最少由 f[i-j^2] 个完全平方数表示，且计算 f(i) 时，其前面的数所需的最少完全平方数是已知的
对所有的 j 进行遍历，找到最少的 i - j^2 对应的最少完全平方数 f[i-j^2]
则 f(i) = 1 + min_j{f[i - j^2]}
//注意若 i 本身为一个完全平方数，则 j = 根号 i 时, dp[i-j^2] = dp[0] = 0
'''
print(Solution().numSquares(13))