"""
approach: iterate through intervals list 
-> if first and second elem are smaller than first elem of new interval or larger than second elem of new interval, append to res
-> if first elem is 
"""
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res: list(list(int)) = []
        i: int = 0
        n: int = len(intervals)
        # case for left end of interval array/when btoh elems are < than elem in newInterval
        while i<n and intervals[i][1]<newInterval[0]:
            res.append(intervals[i])
            i+=1            
        # case for first elem of intervals<newInterval[0] and second elem of intervals>newInterval[0]
        while i<n and intervals[i][0]<=newInterval[1]:
            newInterval[0] = min(intervals[i][0],newInterval[0])
            newInterval[1] = max(intervals[i][1],newInterval[1])
            i+=1
        res.append(newInterval)
        # case for extreem right end of intervals
        while i<n:
            res.append(intervals[i])
            i+=1
        return res