"""
插入排序：前面的视为已排序完成的序列。若遇到比已排序完成的序列更大的，直接加入进去。
否则插入到待排序位置上
使用while循环代码更简洁
"""

def insert_sort(nums):
    n = len(nums)
    # 第1个视为有序
    for i in range(1,n):
        j = i
        target = nums[i]
        while target < nums[j-1] and j > 0:
            nums[j] = nums[j-1]
            j -= 1
        nums[j] = target
        print(nums)


nums = [0,2,1,0,7,4,3,2,7,6,8,12,5]
insert_sort(nums)