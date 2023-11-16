class Solution:
    def findAnagrams(self, s: str, p: str):
        if len(s) < len(p):
            return []
        m = len(p)
        pp = sorted(p)
        ans = []
        for idx, ch in enumerate(s):
            tmp = s[idx:idx+m]
            if sorted(tmp) == pp:
                ans.append(idx)

        return ans



print(Solution().findAnagrams("abab","abc"))