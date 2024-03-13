def bubble_sort(nums):
    n = len(nums)
    for i in range(n-1):
        for j in range(i+1,n):
            if nums[i] > nums[j]:
                nums[i],nums[j] = nums[j],nums[i]
    print(nums)

bubble_sort([3,2,4,1,5,0,2,3,45,3,9])
