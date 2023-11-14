# personal implementation of quick sort
def fast_sort(nums):
    def partition(left, right):
        if left >= right: return
        i, j = left, right
        while i < j:
            while i < j and nums[j] >= nums[left]: j -= 1
            while i < j and nums[i] <= nums[left]: i += 1
            nums[i], nums[j] = nums[j], nums[i]
        nums[i], nums[left] = nums[left], nums[i]
        partition(left, i - 1)
        partition(i + 1, right)

    partition(0, len(nums) - 1)


def bubble_sort(nums):
    # TODO
    pass


def selection_sort(nums):
    # TODO
    pass


def merge_sort(nums):
    # TODO
    pass
