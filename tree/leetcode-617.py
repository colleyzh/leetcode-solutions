"""
leetcode 617. Merge Two Binary Trees

case1: if root1 == null then return root2
case2: if root2 == null then return root1
"""


class Solution:
    def mergeTrees(self, root1, root2):
        if not root1:
            return root2
        if not root2:
            return root1

        root1.val += root2.val
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)
        return root1

    def mergeTrees_iterative(self, root1, root2):
        if not root1:
            return root2
        if not root2:
            return root1
        # stack=[]
        stack = [[root1, root2]]

        while stack:
            cur = stack.pop()
            if not cur[0] or not cur[1]:
                continue

            cur[0].val += cur[1].val

            if cur[0].left == None:
                cur[0].left = cur[1].left
            else:
                stack.append([cur[0].left, cur[1].left])
            if cur[0].right == None:
                cur[0].right = cur[1].right
            else:
                stack.append([cur[0].right, cur[1].right])

        return root1
