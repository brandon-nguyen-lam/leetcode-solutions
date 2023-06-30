'''
55. Jump Game

https://leetcode.com/problems/jump-game/description/

For this question, we will use the greedy approach.
How we will accomplish this is we will start from the beginning
of our array and then at each step, we will update our variable
named cur. This cur value represents the current furthest distance
that we can jump so we want to store the max jump. Since each jump
loses 1 each time we move an index, we want to take the max of
the current max - 1 and then the current position. If our value ever falls
to 0 or equals it, that means we can't jump anymore. If we were able to reach
the end of our array, that means that we were able to jump all the way there.
'''
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cur = nums[0]
        pos = 0

        while pos < len(nums) - 1:
            cur = max(cur - 1, nums[pos])
            if cur <= 0:
                return False
            pos += 1

        return True
        
#T: O(N)
#S: O(1)