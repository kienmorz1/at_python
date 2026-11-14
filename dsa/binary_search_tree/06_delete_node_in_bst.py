"""LeetCode 450 - Delete Node in a BST (recursive solution).

Delete the node with value key (if present) and return the root of the updated BST.
"""
from tree_utils import build_tree, inorder, to_list


class Solution:
    def deleteNode(self, root, key):
        """
        :type root: Optional[TreeNode]
        :type key: int
        :rtype: Optional[TreeNode]
        """
        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            curr = root.right
            while curr.left:
                curr = curr.left

            root.val = curr.val
            root.right = self.deleteNode(root.right, curr.val)

        return root


if __name__ == "__main__":
    sol = Solution()
    root = build_tree([5, 3, 6, 2, 4, None, 7])
    root = sol.deleteNode(root, 3)
    print(to_list(root))  # [5, 4, 6, 2, None, None, 7]
    print(inorder(root))  # [2, 4, 5, 6, 7]
    assert inorder(root) == [2, 4, 5, 6, 7]

    assert sol.deleteNode(build_tree([]), 1) is None
    assert sol.deleteNode(build_tree([1]), 1) is None
    print("all checks passed")
