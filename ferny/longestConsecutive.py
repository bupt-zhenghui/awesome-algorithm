class Solution:
    def longestConsecutive(self, nums) -> int:
        # 用哈希表存储每个端点对应的连续区间的长度
        # 当数不在哈希表中时，取比它小1的左边的连续数组的长度和比它大1的连续数组的长度。
        # 注意要对左边数组的长度和右边数组的长度进行更新
        if len(nums) == 0:
            return 0
        dic = {}
        max_length = 1
        for i in range(len(nums)):
            if nums[i] not in dic:
                left = dic.get(nums[i]-1, 0)
                right = dic.get(nums[i] + 1, 0)
                cur = left + right + 1
                dic[nums[i]] = cur

                max_length = max(max_length,cur)
                # 接下来要更新区间两端点的长度值
                dic[nums[i] - left] = cur
                dic[nums[i] + right] = cur
        return max_length

print(Solution().longestConsecutive([1,2,0,1]))





















# print(Solution().longestConsecutive([100,99,98,0,3,4,5,6]))
