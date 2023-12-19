class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        L,R = [0]*n,[0]*n
        ans = []
        L[0],R[0] = 1,1
        for i, num in enumerate(nums[:n-1]):
            L[i+1] = L[i]*num
        new_nums = nums[::-1]
        for i, num in enumerate(new_nums[:n-1]):
            R[i+1] = R[i]*num
        print(L)
        print(R)
        for i in range(n):
            ans.append(L[i]*R[n-i-1])
        return ans


print(Solution().productExceptSelf([1,2,3,4,5]))


