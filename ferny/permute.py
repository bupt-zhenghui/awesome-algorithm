"""
46. 回溯算法/全排列
递归，仔细想去吧
"""


class Solution:
    def permute(self, nums):
        self.ans = []

        def recur(arr, res):
            if not arr:
                self.ans.append(res)
                return

            for i, num in enumerate(arr):
                tmp = res[:]+[num]
                recur(arr[:i]+arr[i+1:],tmp)
        # 注意这里的arr不能更改，以及res也不能更改，因为递归回来后要保持原有的数据。
        """
        写成下面的形式就错了
            for i ,num in enumerate(arr):
                tmp = res[]+[num]
                arr = arr[:i]+arr[i+1:]  //这里实际上对 arr进行了更改，回溯过程就会出错
                recur(arr,tmp)
        写成下面的形式同样也错误
            for i,num in enumerate(arr):
                res = res[:]+[num]    //这里对result(res)进行了更改，回溯过程也会出错
                recur(arr[:i]+arr[i+1:],res)
        """
        recur(nums, [])
        return self.ans


print(Solution().permute([1, 2, 3]))
