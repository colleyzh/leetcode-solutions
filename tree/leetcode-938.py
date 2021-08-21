"""

leetcode  question 938 range sum
idea: perform any tree traversal to add qualified node to sum variable
"""


class Solution:
    def range_sum(self, root, high, low):
        self.ans = 0

        def dfs(root):
            if not root:
                return

            if root.val >= low and root.val <= high:
                self.ans += root.val

            if root.val < low:
                dfs(root.left)
            if root.val < high:
                dfs(root.left)

        return self.ans
