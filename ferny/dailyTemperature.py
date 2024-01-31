class Solution:
    def dailyTemperatures(self, temperatures):
        if len(temperatures) == 1: return [0]
        stack = []
        ans = [0]*len(temperatures)
        stack.append((temperatures[0],0))
        i = 1
        while i <= len(temperatures)-1:
            x,y = stack[-1]
            if temperatures[i] > x:
                stack.pop()
                # ans.append(i-y)
                ans[y] = i-y
                # 注意弹出的气温要放到对应的位置上
                # 序号直接相减表示间隔的天数
                while stack:
                    x1,y1 = stack[-1]
                    if temperatures[i] > x1:
                        stack.pop()
                        # ans.append(i-y1)
                        ans[y1] = i - y1
                    else:
                        break
                stack.append((temperatures[i],i))
            else:
                stack.append((temperatures[i],i))
                # 在栈里放着的是(每日气温，在数组中对应的序号)
            i = i + 1
        return ans




print(Solution().dailyTemperatures([73,74,75,71,69,72,76,73]))

