class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        return self.help(root, float("-inf"), float("inf"))

    def help(self, root, low, high):

        if not root:
            return True

        if root.val <= low or root.val >= high:
            return False
        left = self.help(root.left, low, root.val)
        right = self.help(root.right, root.val, high)
        return left and right

    def isValidBST2(self, root):
        res = []

        self.inorder(root, res)

        for i in range(1, len(res)):
            if res[i - 1] >= res[i]:
                return False
        return True

    def inorder(self, root, res):
        if not root:
            return

        self.inorder(root.left, res)
        res.append(root.val)
        self.inorder(root.right, res)
