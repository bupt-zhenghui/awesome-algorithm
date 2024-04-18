"""
快速排序，每次都找到一个哨兵，使其左边的值都小于它，右边的值都大于它。
O(nlogn)
"""


def quick_sort(nums, left, right):
    if left >= right:
        return
    # 不要忘记递归终止条件
    l, r = left, right
    pivot = nums[left]
    while l < r:
        while l < r and nums[r] >= pivot:
            r -= 1
        while l < r and nums[l] <= pivot:
            l += 1
        nums[l], nums[r] = nums[r], nums[l]

    nums[l], nums[left] = nums[left], nums[l]

    quick_sort(nums, left, l - 1)
    quick_sort(nums, l + 1, right)
    print(nums)


nums = [0, 2, 1, 0, 7, 4, 3, 2, 7, 6, 8, 12, 5]
left = 0
right = len(nums) - 1
quick_sort(nums, left, right)
