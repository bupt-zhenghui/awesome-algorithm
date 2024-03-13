"""
34. 在数组中查找元素的第1个和最后一个位置
注意：在二分查找中找到第1个target和最后一个 target这种题目，不能用等号判断，而要执行不等号判断
"""
class Solution:
    def searchRange(self, nums, target):
        if not nums:
            return [-1,-1]
        ans = []
        # 先从左边找到第1个>=target的
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l+r)//2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        if l < len(nums) and nums[l] == target:
            ans.append(l)
        else:
            ans.append(-1)

        # 再从右边找到第1个<=target的
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left+right) // 2
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        if right >= 0 and nums[right] == target:
            ans.append(right)
        else:
            ans.append(-1)

        return ans
print(Solution().searchRange([2,2],3))