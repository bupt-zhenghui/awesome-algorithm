class Solution:
    def findAnagrams(self, s: str, p: str):
        if len(s) < len(p):
            return []
        m,n  = len(s), len(p)
        s_count, p_count = [0]*26, [0]*26
        # 从0~25分别代表 a~z. val 代表出现的频次
        # 用数组存储字符串 p 中所有字符以及其出现的频次
        ans = []
        for i in range(n):
            p_count[ord(p[i]) - 97] = p_count[ord(p[i]) - 97] + 1
            s_count[ord(s[i]) - 97] = s_count[ord(s[i]) - 97] + 1

        if p_count == s_count:
            ans.append(0)

        for idx in range(m - n):

            s_count[ord(s[idx]) - 97] -= 1
            # 去掉滑动窗口左端对应的字符
            s_count[ord(s[idx + n]) - 97] += 1
#             增加滑动窗口右端对应的字符
            if s_count == p_count:
                ans.append(idx + 1)

        return ans

print(Solution().findAnagrams("aa","bb"))