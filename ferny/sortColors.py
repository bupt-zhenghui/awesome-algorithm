"""
75. 颜色分类
1. 排序
2. 单指针
"""
class Solution:
    def sortColors(self, nums) -> None:
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i+1,n):
        #         if nums[j] < nums[i]:
        #             nums[i],nums[j] = nums[j],nums[i]
        #     print(nums)
        # print("------------------")
        # return nums
        pre = 0
        for idx, num in enumerate(nums):
            if nums[idx] == 0:
                nums[pre],nums[idx] = nums[idx],nums[pre]
                pre += 1

        for i in range(pre,len(nums)):
            if nums[i] == 1:
                nums[pre],nums[i] = nums[i],nums[pre]
                pre += 1




print(Solution().sortColors([2,0,2,1,1,0,0,1,2]))