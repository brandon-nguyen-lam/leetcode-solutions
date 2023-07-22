'''
128. Longest Consecutive Sequence

https://leetcode.com/problems/longest-consecutive-sequence/description/

We can make clever use of how sets work in Python to solve this problem.
The idea is that we want to iterate through each number in our array and
then check if the number before it exists in our set. If it doesn't, that means
that we are at the beginning of a sequence. From there, we can keep track of
the current count and then keep incrementing it until we reach the end of the
sequence. We can then update our result with the max of the current result and
the current count. We can then return the result.
'''


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0

        for num in nums:

            if num - 1 not in nums:
                temp = num
                cur_count = 1
                while temp in nums:
                    res = max(res, cur_count)
                    cur_count += 1
                    temp += 1

        return res

# T: O(N)
# S: O(N)