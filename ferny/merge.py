class Solution:
    def merge(self, intervals):
        if len(intervals) == 1:
            return intervals
        intervals.sort()
#         会直接按照每个数组第一个的大小排序，好神奇！
#         print(intervals)
        ans = [intervals[0]]
        # ans是一个二元数组，ans[-1][1]表示最后一行的第2个数
        # l, r分别为interval[i]的第一位和第二位
        for l, r in intervals[1:]:
            if l > ans[-1][1]:
                ans.append([l,r])
            else:
                if r > ans[-1][1]:
                    ans[-1][1] = r
        return ans



print(Solution().merge([[1,4],[0,5],[2,3],[10,11],[4,6]]))