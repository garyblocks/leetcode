# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

import types
class Solution(object):
    def merge(self, intervals):
        size = len(intervals)
        i = 0
        #def __repr__(self): return repr([self.start, self.end])  
        #setattr(Interval,'__repr__',__repr__)
        intervals.sort(key=lambda k: k.start)
        while i<size and i+1<size:
            if intervals[i+1].start < intervals[i].start:
                intervals[i+1],intervals[i]=intervals[i],intervals[i+1]
            if intervals[i+1].end>=intervals[i].end>=intervals[i+1].start:
                intervals[i].end = intervals[i+1].end
                intervals.pop(i+1); size-=1
            elif intervals[i+1].end<intervals[i].end:
                intervals.pop(i+1); size-=1
            else:
                i+=1
        return intervals
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """