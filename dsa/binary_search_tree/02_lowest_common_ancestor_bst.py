"""LeetCode 235 - Lowest Common Ancestor of a Binary Search Tree (recursive solution).

Given a BST and two nodes p and q (both exist in the tree), return their lowest common ancestor.
A node may be an ancestor of itself.
"""
from tree_utils import TreeNode, build_tree


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return root


if __name__ == "__main__":
    sol = Solution()
    root = build_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    p = TreeNode(2)  # compared by value only
    q = TreeNode(8)
    print(sol.lowestCommonAncestor(root, p, q).val)  # 6

    node2 = root.left         # value 2
    node4 = root.left.right   # value 4
    print(sol.lowestCommonAncestor(root, node2, node4).val)  # 2
    assert sol.lowestCommonAncestor(root, p, q).val == 6
    assert sol.lowestCommonAncestor(root, node2, node4).val == 2
    print("all checks passed")
