class Solution:
    def threeSum(self, nums):
        nums.sort()
        new_set = set()
        if nums[0] > 0 or nums[-1] < 0: return []
        if nums[0] == nums[-1] == 0: return [[0,0,0]]
        for j in range(1, len(nums) - 1):
            i, k = 0, len(nums) - 1
            while i < j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    if (nums[i], nums[j], nums[k]) not in new_set:
                        new_set.add((nums[i], nums[j], nums[k]))
                    k = k - 1
                    i = i + 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k = k - 1
                else:
                    i = i + 1

        return list(new_set)



print(Solution().threeSum([-1,0,1,2,-1,-4]))