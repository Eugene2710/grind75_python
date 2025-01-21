"""
approach:
- if newInterval[0] is >= interval[n][0] and newInterval[1] <= interval[n][1]: return intervals break
- if newInterval[0] is < interval[n][0] and newInterval[1] < interval[n][1]: res.append(newInterval), res.append(intervals[n])
    iterate to the end of interval array
- if newInterval[0] is > interval[n][0] and newInterval[1] < interval[n][1]: return intervals


intervals = [[1,3],[6,9]], newInterval = [2,5] [0,5]
intervals = [[2,3],[6,9]], newInterval = [0,1]

[2,5]   [2,6]

"""
class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        res: list(list(int)) = []
        for i in intervals:
            if intervals[i][1] < newInterval[0]:
                res.append(intervals[i])
            else:
                break
                
        for j in range(i,n):
            if intervals[j][0] <= newInterval[1]:
                newInterval[0] = min(intervals[j][0], newInterval[0])
                newInterval[1] = max(intervals[j][1], newInterval[1])
            else:
                break
        res.append(newInterval)

        for k in range(j+1,n):
            res.append(intervals[k])

        return res