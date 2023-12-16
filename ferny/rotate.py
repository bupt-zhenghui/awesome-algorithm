class Solution:
    def rotate(self, nums, k):
        n = len(nums)
        nums.reverse()
        left = 0
        right = k % n-1
        while left <= right:
            nums[left],nums[right] = nums[right],nums[left]
            left += 1
            right -= 1

        l = k % n
        r = n - 1
        while l <= r:
            nums[l],nums[r] = nums[r],nums[l]
            l += 1
            r -= 1




Solution().rotate([1,2,3,4,5,6,7],3)
