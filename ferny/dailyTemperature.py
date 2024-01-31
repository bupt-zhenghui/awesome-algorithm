class Solution:
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        idx = 1
        stack = []
        stack.append(0)
        ans = [0]*n
        idxpre = 0
        while idx < n:
            if temperatures[idx] > temperatures[idxpre]:
                ans[idxpre] = idx - idxpre
                stack.pop()
                if stack:
                    idxpre = stack[-1]
                    while stack:
                        if temperatures[idx] > temperatures[idxpre]:
                            ans[idxpre] = idx - idxpre
                            stack.pop()
                            idxpre -= 1
                        else:
                            break
            stack.append(idx)
            idx += 1
            idxpre = stack[-1]
        return ans

print(Solution().dailyTemperatures([73,74,75,71,69,72,76,73]))

