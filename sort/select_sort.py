"""
选择排序的思想：首先在未排序序列中找到最大/最小的元素，放在第一个位置；
然后在[1,n]中选择最大/最小的元素，放在第二个位置。以此类推。
"""


def select_sort(nums):
    n = len(nums)
    for i in range(n):
        idx = i
        min_num = nums[i]
        for j in range(i + 1, n):
            if nums[j] < min_num:
                min_num = nums[j]
                idx = j
        nums[i], nums[idx] = nums[idx], nums[i]
    print(nums)


select_sort([3, 4, 23, 5, 3, 1, 0, 3, 4, 8, 19])
