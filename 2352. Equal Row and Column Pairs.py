'''
2352. Equal Row and Column Pairs

https://leetcode.com/problems/equal-row-and-column-pairs/

A rather self explanatory problem. Basically, if we ever have
an entire row that is equal to an entire column, we will add 1
to our count. Our goal is to count the amount of columns that equal
one another.

My implementation uses a hashmap, and the idea behind this is that
we are going to count each row and for each row, we will have it so
that the hashmap key is the actual array and then the value will be
the amount of times it shows up. The reasoning it is the amount of
times that it shows up versus just being 1 is that this handles any
case where we have to deal with duplicates.

'''
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows = defaultdict(int)
        res = 0
        
        for r in range(len(grid)):
            cur = []
            for c in range(len(grid[0])):
                cur.append(grid[r][c])
            rows[tuple(cur)] += 1

        for c in range(len(grid[0])):
            cur = []
            for r in range(len(grid)):
                cur.append(grid[r][c])

            if tuple(cur) in rows: res += rows[tuple(cur)]
        
        return res

#T: O(N^2)
#S: O(N^2)