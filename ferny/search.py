"""
33. 搜索螺旋排序数组
每一次分割，都会将数组分为1个有序数组和1个无序数组
"""
class Solution:
    def search(self, nums, target):
        n = len(nums)
        l, r = 0, n-1
        while l <= r:
            mid = (l+r) // 2
            if nums[mid] == target:
                return mid
            if nums[l] <= nums[mid]:
                # 如果切分的左边有序且目标值在有序序列中
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                # 如果切分的右边有序且目标值在有序序列中
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1


        return -1

print(Solution().search([4,5,6,7,0,1,2],3))