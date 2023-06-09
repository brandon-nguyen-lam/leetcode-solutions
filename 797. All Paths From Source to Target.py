'''
797. All Paths From Source to Target

https://leetcode.com/problems/all-paths-from-source-to-target/description/

This problem is a pretty standard backtracking problem. We can notice that
we will always be starting at 0 and then trying to reach our target value which
is going to be n - 1.

When thinking about doing backtracking, there are a couple of things that we need
to recognize.

1.) What's our base case?
Well, whenever we reach the node at n - 1 we are going to want to return. We need
to return all paths that reach there so what we can do is append our current path
we are keeping track of to some res variable at the end.

2.) What are our decisions?
Our decisions are pretty simple, we have only two outcomes. One where we decide to use a path
and then one where you don't decide to use the path. A simple append and pop can handle the cases
for that. Now all we need to do is start from 0 and then run through all cases of backtracking
for a quick and simple solution.
'''
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []

        def backtrack(cur_idx = 0, cur_path = [0]):
            if cur_idx == len(graph) - 1:
                res.append(cur_path[:])
                return

            for neighbor in graph[cur_idx]:
                cur_path.append(neighbor)
                backtrack(neighbor, cur_path)
                cur_path.pop()

        backtrack()
        return res

#T: O(2^N * N)
#S: O(N)