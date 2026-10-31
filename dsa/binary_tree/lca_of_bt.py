from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int = 0):
        self.val = val
        self.left: Optional['TreeNode'] = None
        self.right: Optional['TreeNode'] = None


class Solution:
    def lowestCommonAncestor(
        self, root: Optional[TreeNode], p: TreeNode, q: TreeNode
    ) -> Optional[TreeNode]:
        """
        Finds the Lowest Common Ancestor of two nodes in a binary tree.
        """
        # Base condition: empty branch or target node found
        if root is None or root == p or root == q:
            return root

        # Divide step: search left and right subtrees
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # Conquer step:
        # Case 1: p and q are in different subtrees, current node is the LCA
        if left is not None and right is not None:
            return root

        # Case 2: both nodes are in the left or right subtree (or only one was found)
        return left if left is not None else right


# --- Driver Code and Verification ---
if __name__ == "__main__":
    """
    Constructing the example binary tree:
             3
           /   \
          5     1
         / \   / \
        6   2 0   8
           / \
          7   4
    """
    # 1. Instantiate tree nodes
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)

    # 2. Assign targets
    target_p = root.left        # Node(5)
    target_q = root.right       # Node(1)
    target_q2 = root.left.right.right  # Node(4)

    solver = Solution()

    # Case A: Targets in different subtrees (5 and 1)
    lca_a = solver.lowestCommonAncestor(root, target_p, target_q)

    # Case B: One target is ancestor of the other (5 and 4)
    lca_b = solver.lowestCommonAncestor(root, target_p, target_q2)

    # 3. Print outputs
    print(f"LCA of Node(5) and Node(1): {lca_a.val if lca_a else None}")
    print(f"LCA of Node(5) and Node(4): {lca_b.val if lca_b else None}")