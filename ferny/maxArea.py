class Solution:
    def maxArea(self, height):
        maxarea = 0
        l,r = 0,len(height)-1
        # 双指针例题
        tmp = min(height[l], height[r]) * (r - l)
        maxarea = max(maxarea, tmp)
        while l < r:
            k = min(height[l],height[r])
            # 关键：固定一个最小值
            if k == height[l]:
                l = l + 1
                # tmp = min(height[l],height[r])*(r-l)
                # maxarea = max(tmp,maxarea)
            else:
                r = r - 1
            tmp = min(height[l],height[r])*(r-l)
            maxarea = max(tmp,maxarea)

        return maxarea

print(Solution().maxArea([2,3,4,5,18,17,6]))
