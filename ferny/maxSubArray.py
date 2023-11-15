# 53. 最大子数组和

class Solution:
    def maxSubArray(self, nums):
        posi = []
        for i in range(len(nums)):
            if nums[i] > 0:
                posi.append(i)
#         找出所有值为正的坐标
        if not posi:
            nums.sort()
            return nums[-1]
        if len(posi) == 1:
            return nums[posi[0]]

        max_total = 0
        for i, idx in enumerate(posi):
            for j in posi[i+1:]:
                total = sum(nums[idx:j+1])
                max_total = max(max_total,total)

        nums.sort()
        return max(max_total,nums[-1])

print(Solution().maxSubArray([3,-3,2,-3]))




