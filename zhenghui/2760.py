class Solution:
    def longestAlternatingSubarray(self, nums, threshold: int) -> int:
        idx = ans = 0
        while idx < len(nums):
            if nums[idx] % 2 != 0 or nums[idx] > threshold:
                idx += 1
                continue
            tmp = idx
            while tmp < len(nums) - 1 and (nums[tmp] + nums[tmp + 1]) % 2 != 0 \
                    and nums[tmp] <= threshold and nums[tmp + 1] <= threshold:
                tmp += 1
            ans = max(ans, tmp - idx + 1)
            idx = tmp + 1
        return ans
