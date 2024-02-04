class Solution:
    def wordBreak(self, s: str, wordDict):
        dp = [False]*(len(s)+1)
        dp[0] = True
        # dp[0]表示空字符可以被字典中的单词表示
        n = len(s)
        for i in range(n):
            for j in range(i+1,n+1):
                if dp[i] and s[i:j] in wordDict:
                    dp[j] = True

        return dp[-1]

        # dp = [False]*(len(s)+1)
        # dp[0] = True
        # for i in range(1,len(s)+1):
        #     for j in range(i):
        #         if dp[j]:
        #             for word in wordDict:
        #                 if s[:j] + word == s[:i]:
        #                     dp[i] = True
        #                     break
        #         if dp[i] == True: break
        # return dp[-1]
"""
可以用True or False 定义 前dp[i]个单词是否可以被表示

"""


print(Solution().wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))



