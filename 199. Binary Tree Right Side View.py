'''
199. Binary Tree Right Side View

https://leetcode.com/problems/binary-tree-right-side-view/

The problem is quite self explanatory, just imagine that you had
a binary tree structure and that you were standing on the right side of it.
From there, how can we achieve that? Well, the first thing that comes to mind is
BFS since we can achieve level order traversal. Going level by level will mean
that we can get the right side value each time by reaching the end of the level.

There's no clever/faster way to solve this problem in specific, you need to
visit every node to see its left and right neighbors. Just create a deque
and then traverse each level until we are at the final node. Once we are
there, we can append to our return array.

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []

        queue = deque([root])
        res = []

        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)

            res.append(node.val)
        return res
            
#T: O(N)
#S: O(N)
        
        