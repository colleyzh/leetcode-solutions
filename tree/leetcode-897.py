"""
897. Increasing Order Search Tree

idea: use inorder traversal. so the num will be sorted. then create a new tree

"""


class Solution:
    def increasingBST(self, root):
        stack = []
        self.inorder(root, stack)

        res = cur = TreeNode(None)
        for node in stack:
            cur.right = TreeNode(node)
            cur = cur.right
        return res.right

    def inorder(self, root, stack):

        if not root:
            return

        self.inorder(root.left, stack)
        stack.append(root.val)
        self.inorder(root.right, stack)
