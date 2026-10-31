from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x: int):
        self.val = x
        self.left: Optional['TreeNode'] = None
        self.right: Optional['TreeNode'] = None


class Solution:
    def solve(self, A: Optional[TreeNode], B: int) -> List[int]:
        """
        Finds the path from the root node to the node with value B.
        """
        path: List[int] = []

        def findPath(node: Optional[TreeNode], target: int) -> bool:
            # Base condition: empty node branch hit
            if node is None:
                return False

            # Add current node to candidate path
            path.append(node.val)

            # Target found
            if node.val == target:
                return True

            # Explore child branches
            if findPath(node.left, target) or findPath(node.right, target):
                return True

            # Backtrack: target is not present in subtrees of this node
            path.pop()
            return False

        findPath(A, B)
        return path


# --- Driver Code and Verification ---
if __name__ == "__main__":
    """
    Constructing the example binary tree:
             1
           /   \
          2     3
         / \   / \
        4   5 6   7
    """
    # 1. Instantiate tree nodes
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    # 2. Search for path to target node 5
    solver = Solution()
    target = 5
    result_path = solver.solve(root, target)

    # 3. Print output
    print(f"Path to node {target}: {result_path}")