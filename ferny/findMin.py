"""
153. 寻找旋转排序数组中的最小值
"""
class Solution:
    def findMin(self, nums):
        n = len(nums)
        if nums[0] < nums[n-1]:
            return nums[0]
        if len(nums) == 2:
            return min(nums[0],nums[1])
        l, r = 0, n-1
        min_num = nums[0]

        while l <= r:
            mid = (l+r) // 2
            min_num = min(nums[mid], min_num)
            if nums[l] <= nums[mid]:  #l 到 mid 有序
                if not min_num == nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                r = mid - 1

        return min_num


print(Solution().findMin([2,1]))