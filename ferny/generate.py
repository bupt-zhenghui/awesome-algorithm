class Solution:
    def generate(self, numRows):
        if numRows == 1: return [[1]]
        if numRows == 2: return [[1],[1,1]]
        ans = []
        ans.append([1])
        ans.append([1,1])
        for i in range(2,numRows):
            dp = ans[-1]
            dp_new = [0]*(len(dp)+1)
            dp_new[0],dp_new[-1] = 1,1
            m,n = 0, 1
            for idx, num in enumerate(dp_new[1:-1]):
                dp_new[idx+1] = dp[m]+dp[n]
                m += 1
                n += 1
            ans.append(dp_new)
        return ans


print(Solution().generate(5))