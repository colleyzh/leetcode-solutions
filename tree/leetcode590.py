"""
leetcode:590. N-ary Tree Postorder Traversal



"""


class Solution:
    def postorder(self, root: "Node") -> List[int]:
        output = []
        self.dfs(root, output)

        return output

    def dfs(self, root, output):
        if not root:
            return

        output.insert(0, root.val)

        for node in root.children[::-1]:
            self.dfs(node, output)

    def postorder(self, root: "Node") -> List[int]:
        if not root:
            return []

        stack = [root]
        output = []

        while stack:
            node = stack.pop()
            output.insert(0, node.val)

            for val in node.children:
                stack.append(val)

        return output
