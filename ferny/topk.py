"""
用堆排序实现topk问题
"""
import heapq
nums = [3,2,5,1,4,7,8]
k = 3
heapq.heapify(nums)
for i in range(len(nums) - k):
    heapq.heappop(nums)

print(nums)
