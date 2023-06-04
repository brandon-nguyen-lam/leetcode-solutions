'''
744. Find Smallest Letter Greater Than Target

https://leetcode.com/problems/find-smallest-letter-greater-than-target/description/

We are given a target letter and we have to find the smallest value that is
still has a higher lexographical value than it. So for example if our target was
the letter 'b' and we had a letters array of ['b', 'c', 'd']. We would return the value
'c' at the end because it is the smallest value GREATER than 'b'. If there is no value
possible then we must return letters[0].

One thing to note is that the array is sorted so we can look into trying to do
binary search. When we think of binary search, let's think of the true and false
cases.

True:
- The lexographical value of our mid value is greater than our target

False:
- The lexographical value of our mid value is lower than our target
'''
# Brute Force
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        target_ascii = ord(target) - ord('a')
        smallest_letter = math.inf
        res = letters[0]

        for ch in letters:
            ch_ascii = ord(ch) - ord('a')
            
            diff = ch_ascii - target_ascii

            if diff <= 0: continue
            if diff == 1: return ch

            if diff < smallest_letter:
                smallest_letter = diff
                res = ch

        return res

#T: O(N)
#S: O(1)

# Binary Search
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l, r = 0, len(letters) - 1

        while l <= r:
            m = (l + r) // 2

            if letters[m] <= target:
                l = m + 1
            else: # letters[m] > target
                r = m - 1

        if l == len(letters): return letters[0]
        else: return letters[l]

#T: O(Log N)
#S: O(1)