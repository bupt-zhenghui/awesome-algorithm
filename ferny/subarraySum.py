class Solution:
    def subarraySum(self, nums, k):
        presum = {}
#         此字典用于统计所有前缀和出现的次数
        presum[0] = 1
        total = 0
#         表示以i结束的连续数组的和 (共 i + 1 项)
        count = 0
        for i, num in enumerate(nums):
            total = total + num
            #  表示存在由 j 到 i， 此子数组的和为 k。此时并不知道 j ，只知道在前面出现了几次
            if total - k in presum:
                count = count + presum[total - k]

            if total in presum:
                presum[total] += 1
            else:
                presum[total] = 1

        return count

print(Solution().subarraySum([1,1,1], 2))
