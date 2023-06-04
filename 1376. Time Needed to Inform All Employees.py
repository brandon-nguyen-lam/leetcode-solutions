'''
1376. Time Needed to Inform All Employees

https://leetcode.com/problems/time-needed-to-inform-all-employees/

The essence behind this problem is that we have the maximum time that
it would take for us to inform all employees of something. In the problem photo
we can see the structure of how it works. We can recognize that this is a graph
and after realizing that, we can figure out our starting point. We could either
start at the manager and go out or go from each person to the manager. Either way
will work but personally I believe it's easier to go from manager to employees.

The idea behind this will be a Breadth First Search where we go from the manager
and then from there we keep going to the people who are reporting to them and
what we need to do is keep track of the time. Since each person has an 'informTime'
what we can do is start off with a time of 0 at our manager and increase our
current time by the specific employees informTime. On each iteration of this,
we will have a max variable and compare it each time to get our final result.
'''

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = defaultdict(list)
        res = 0

        for i in range(n): 
            if manager[i] != -1:
                graph[manager[i]].append(i)

        queue = deque([(headID, 0)])

        while queue:
            node, time = queue.popleft()
            res = max(time, res)

            for manager in graph[node]:
                queue.append((manager, time + informTime[node]))
        
        return res

#T: O(N)
#S: O(N)

                
