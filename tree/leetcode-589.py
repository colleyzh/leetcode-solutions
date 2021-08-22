"""
leetcode 589. N-ary Tree Preorder Traversal
caution: it is not giving left node and right node. it gives a list of children node


"""


class Solution:
    def preorder(self, root: "Node") -> List[int]:

        stack = []
        if not root:
            return []

        stack.append(root)
        res = []
        while stack:
            node = stack.pop()
            res.append(node.val)
            stack.extend(node.children[::-1])

        return res

    def preorder(self, root: "Node") -> List[int]:

        output = []
        self.dfs(root, output)

        return output

    def dfs(self, root, stack):
        if not root:
            return

        stack.append(root.val)

        for node in root.children:
            self.dfs(node, stack)
