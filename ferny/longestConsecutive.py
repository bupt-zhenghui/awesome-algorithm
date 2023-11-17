class Solution:
    def longestConsecutive(self, nums) -> int:
        if len(nums) == 0:
            return 0
        num_set = set(nums)
        new_set = set()
        max_length = 0
        length = 1
        i = 0
        while i < len(nums):
            tmp = nums[i]
            if tmp not in new_set:
                while length < len(nums):
                    if tmp + 1 in num_set:
                        new_set.add(tmp)
                        tmp += 1
                        length += 1
                    else:
                        new_set.add(tmp)
                        break
            # print(new_set)
            max_length = max(max_length, length)
            length = 1
            # print(f"max_length: {max_length}, length: {length}")
            i = i + 1

        return max_length

print(Solution().longestConsecutive([100,99,98,0,3,4,5,6]))
