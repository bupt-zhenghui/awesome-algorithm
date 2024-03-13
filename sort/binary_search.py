"""
二分查找是在有序数组中查找指定的元素所在的位置，若元素不在该有序数组中，则返回其应该插入的位置
复杂度为 logn
"""

def binary_search(nums,target):
    l, r = 0, len(nums)-1
    while l <= r:
        mid = (l+r) // 2
        if nums[mid] == target:
            print(mid)
            return
        elif nums[mid] > target:
            r = mid - 1
        else:
            l = mid + 1

    # 若不存在，表示插入在该序数之前
    print(l)

nums = [0, 0, 2, 3, 4, 5, 6, 8, 10, 12, 66, 90]
target = 88
binary_search(nums,target)