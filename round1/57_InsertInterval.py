# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        size = len(intervals)
        i = 0
        if size==0:
            intervals.append(newInterval)
            return intervals
        while i < size:
            if newInterval.start>intervals[i].start and newInterval.end<intervals[i].end:
                break
            elif intervals[i].start<=newInterval.start<=intervals[i].end:
                newInterval.start = intervals[i].start
                newInterval.end = max(intervals[i].end, newInterval.end)
                intervals.pop(i); size-=1
                if i==size:
                    i-=1
            elif intervals[i].start<=newInterval.end<=intervals[i].end:
                newInterval.end = intervals[i].end
                newInterval.start = min(intervals[i].start, newInterval.start)
                intervals.pop(i); size-=1
                if i==size:
                    i-=1
            elif newInterval.start<=intervals[i].start and newInterval.end>=intervals[i].end:
                intervals.pop(i); size-=1
                if i==size:
                    i-=1
            elif i-1>=0 and intervals[i].start>newInterval.end and intervals[i-1].end < newInterval.start:
                intervals.insert(i,newInterval)
                break
            elif i==0 and intervals[i].start>newInterval.end:
                intervals.insert(i,newInterval)
                break
            elif i==size-1 and intervals[i].end<newInterval.start:
                intervals.append(newInterval)
                break
            else:
                i+=1
            if size==0:
                intervals.append(newInterval)
                return intervals
        return intervals
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """