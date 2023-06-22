'''
252. Meeting Rooms

https://leetcode.com/problems/meeting-rooms/description/

The goal is to find if we can attend all meetings at once.
We first start off with sorting each element and then 
we will iterate from the start to the end of the list and compare
two elements at a time. These elements will be meeting and then
the next meeting after. Since we sorted each of them, the earlier times
are all at the front. So what we can do is recognize that we just need
to check the end of meeting 1 and the start of room 2 and make sure
that there's no overlap. 

In the case of an overlap, that would be when meeting 2 starts before
the end of meeting 1. If we manage to make it through all meetings,
we can return True.
'''

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()

        if len(intervals) <= 1: return True

        for i in range(len(intervals) - 1):
            r1, r2 = intervals[i], intervals[i + 1]

            if r1[1] > r2[0]: return False

        return True

#T: O(N Log N)
#S: O(1)