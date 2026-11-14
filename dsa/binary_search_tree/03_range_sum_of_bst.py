"""LeetCode 938 - Range Sum of BST (recursive solution).

Return the sum of all node values v such that low <= v <= high.
"""
from tree_utils import build_tree


class Solution:
    def rangeSumBST(self, root, low, high):
        """
        :type root: Optional[TreeNode]
        :type low: int
        :type high: int
        :rtype: int
        """
        if not root:
            return 0

        if root.val < low:
            return self.rangeSumBST(root.right, low, high)

        if root.val > high:
            return self.rangeSumBST(root.left, low, high)
        return (
            root.val +
            self.rangeSumBST(root.left, low, high) +
            self.rangeSumBST(root.right, low, high)
        )


if __name__ == "__main__":
    sol = Solution()
    root = build_tree([10, 5, 15, 3, 7, None, 18])
    print(sol.rangeSumBST(root, 7, 15))  # 32
    print(sol.rangeSumBST(root, 6, 10))  # 17
    assert sol.rangeSumBST(root, 7, 15) == 32
    assert sol.rangeSumBST(root, 6, 10) == 17
    print("all checks passed")
