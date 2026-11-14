"""LeetCode 701 - Insert into a Binary Search Tree (iterative solution).

Insert val into the BST and return the root. The new node is always attached as a leaf.
"""
from tree_utils import TreeNode, build_tree, inorder


class Solution:
    def insertIntoBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        if root is None:
            return TreeNode(val)
        temp = root
        while temp is not None:
            if temp.val > val:
                if temp.left is None:
                    temp.left = TreeNode(val)
                    break
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = TreeNode(val)
                    break
                temp = temp.right
        return root


if __name__ == "__main__":
    sol = Solution()
    root = build_tree([4, 2, 7, 1, 3])
    root = sol.insertIntoBST(root, 5)
    print(inorder(root))  # [1, 2, 3, 4, 5, 7]
    assert inorder(root) == [1, 2, 3, 4, 5, 7]

    empty = sol.insertIntoBST(None, 10)
    assert empty.val == 10
    print("all checks passed")
