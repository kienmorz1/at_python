from typing import Optional
class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        Calculates the maximum depth of a binary tree.
        """
        # Base condition: an empty node has depth 0
        if root is None:
            return 0

        # Divide step: recursively find depth of left and right subtrees
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        # Conquer step: 1 (current node) + maximum of left and right depths
        return 1 + max(left_depth, right_depth)


# --- Driver Code and Verification ---
if __name__ == "__main__":
    """
    Constructing the example binary tree:
             3
            / \
           9  20
              /  \
             15   7
    """
    # 1. Instantiate tree nodes
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    # 2. Compute maximum depth
    solver = Solution()
    depth = solver.maxDepth(root)

    # 3. Print output
    print(f"Maximum depth of the binary tree: {depth}")