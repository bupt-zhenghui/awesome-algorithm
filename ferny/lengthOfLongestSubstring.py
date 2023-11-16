# 3 无重复字符的最长字串

# 动态规划，和最大字串的和一样，寻找以序号为 idx 为结尾的最长不重复字串的长度，建立其与 idx - 1结尾的最长不重复字串的长度之间的关系
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        dp = []
        tmp = 0
        for i, ch in enumerate(s):
            # print(f"i的值为{i},ch的值为{ch}")
            strset = set(s[tmp:i])
            if i == 0:
                dp.append(1)
            if i != 0 and ch not in strset:
                dp.append(dp[i-1]+1)
            else:
                if i != 0:
                    k = i - 1
                    while k >= 0:
                        if s[k] == ch:
                            tmp = k
                            break
                        k = k - 1
                    dp.append(len(s[tmp:i]))
                    tmp = tmp + 1
            # print(dp)
            # print("------------------------------")
        dp.sort()
        return dp[-1]


print(Solution().lengthOfLongestSubstring("pppp"))
