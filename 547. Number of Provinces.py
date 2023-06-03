'''
547. Number of Provinces

https://leetcode.com/problems/number-of-provinces/description/

The problem statement is very simple, find the number of provinces total.
Since the cities all connected to each other equal 1 province, we just
need to find the total number of individual provinces. The first thing
that jumps to mind is Union Find, since it's incredibly easy to do something like
this.

In the first solution, we can see that we start off the union find with the typical
parent and rank and there's nothing special about our union and find functions.
While we are running our algorithm, we will go through the entire list and run
our union command when these criteria exist:
1.) We have a connected city
2.) THe two cities have not been merged yet

Once we merge the two together, we have this variable res that is the total of
all of the cities, if we union together a city, we need to subtract one from it.
After all the unions, we will know what our result is.

For the DFS approach, we first need to populate our adjacency graph and
what we can recognize is that it's bidirectional in the sense that if it's
true for i,j it'll also work for j,i which was the reason I used a set instead
of a list for my dictionary since I didn't want to deal with dupes.

From here, what we can do is run our dfs an 'n' amount of times and increase
our res value by 1 each time and since the dfs will mark anything we've marked
as visited, it will make everything work perfectly at the end.
'''
# Union Find
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        res = len(isConnected)
        n = len(isConnected)
        par = [i for i in range(n)]
        rank = [0] * n

        def find(node):
            if node != par[node]:
                par[node] = find(par[node])
            return par[node]

        def union(x, y):
            x, y = find(x), find(y)

            if rank[x] > rank[y]:
                par[y] = x
                rank[x] += 1
            else:
                par[x] = y
                rank[y] += 1

        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j] and find(i) != find(j):
                    res -= 1
                    union(i, j)
        return res

#T: O(N^2)
#S: O(N)

# DFS
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = set()
        graph = defaultdict(set)
        res = 0

        def dfs(node):
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)

        for i in range(n):
            for j in range(len(isConnected[i])):
                if isConnected[i][j] == 1:
                    graph[i].add(j)
                    graph[j].add(i)

        for i in range(n):
            if i not in visited:
                dfs(i)
                res += 1
                visited.add(i)

        return res

#T: O(N^2)
#S: O(N)
