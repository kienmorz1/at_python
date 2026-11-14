"""LeetCode 700 - Search in a Binary Search Tree (recursive solution).

Given the root of a BST and a value, return the subtree rooted at the node with that value,
or None if it does not exist.
"""
from tree_utils import TreeNode, build_tree, to_list


class Solution:
    def searchBST(self, root, key):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        if root is None:
            return None
        if root.val == key:
            return root
        if root.val > key:
            return self.searchBST(root.left, key)
        return self.searchBST(root.right, key)


if __name__ == "__main__":
    sol = Solution()
    root = build_tree([4, 2, 7, 1, 3])
    found = sol.searchBST(root, 2)
    print(to_list(found))         # [2, 1, 3]
    print(sol.searchBST(root, 5))  # None
    assert to_list(sol.searchBST(root, 2)) == [2, 1, 3]
    assert sol.searchBST(root, 5) is None
    print("all checks passed")
