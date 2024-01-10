class Solution:
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        ans = []
        i = 0
        while i < n-1:
            if temperatures[i+1] > temperatures[i]:
                ans.append(1)
            else:
                pre = i
                post = i + 2
                while post < n:
                    if temperatures[post] > temperatures[pre]:
                        ans.append(post-pre)
                        break
                    else:
                        post += 1
                if post == n:
                    ans.append(0)
            i = i + 1

        ans.append(0)
        return ans

print(Solution().dailyTemperatures([73,74,75,71,69,72,76,73]))

