"""
287. 寻找重复数字[1,n]范围内共有 n+1 个数字，至少存在一个重复数字
使用二分法解决问题？黑人，问号脸
这道题使用二分法是在[1,2,3,...,n]中查找一个整数，而非在输入数组中查找一个整数 l = 1, r = n。分别为数组序列的起始和末尾
若在 mid 之前有重复数字，则 cnt 一定大于mid. mid有可能为重复数字, r = mid 此时在范围[l,mid]中继续查找
若在 mid 之后有重复数字，则 cnt 一定 <= mid。且mid不可能为重复数字， l = l + 1此时在范围[l+1,r]中查找
结束条件 : l >= r
"""
class Solution:
    def findDuplicate(self, nums):
        # 这里的l,r不指序号，二是真实的阿拉伯数字 l = 1, r = n = len(nums)-1
        l,r = 1, len(nums)-1
        while l < r:
            mid = (l + r) // 2
            cnt = 0
            for num in nums:
                if num <= mid:
                   cnt += 1
            if cnt > mid:
                r = mid
            else:
                l = mid + 1
        return l


print(Solution().findDuplicate([1,3,4,2,2]))