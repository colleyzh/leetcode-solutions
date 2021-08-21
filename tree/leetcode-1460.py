"""
leetcode 1469. Find All The Lonely Nodes

traveral the the binary tree
**a lonely node is a node that is the only child of its parent node**
case1:
left node is null  and right node is not null
case2:
right node is null and left node is not null

"""


class Solution:
    def get_longely_node(self, root):
        stack = []
        res = []
        if not root:
            return res
        stack.append(root)
        while len(stack):
            node = stack.pop()
            if node.left and node.right == None:
                res.append(node.left.val)
            if node.right and node.left == None:
                res.append(node.right.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

    def get_longely_node_recursion(self, root):
        res = []
        if not root:
            return res
        self.helper(root, res)
        return res

    def helper(self, root, res):
        if not root:
            return

        if root.left and not root.right:
            res.append(root.left.val)
        if root.right and not root.left:
            res.append(root.right.val)

        self.helper(root.left, res)
        self.helper(root.right, res)
