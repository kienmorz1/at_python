class Node:
    def __init__(self, val: int):
        self.data = val
        self.left = None
        self.right = None


class Solution:
    def height(self, root: Node) -> int:
        """
        Calculates the height (node-based depth) of a binary tree.
        """
        # Base condition: an empty subtree has height 0
        if root is None:
            return 0

        # Divide step: recursively calculate height of left and right subtrees
        left_height = self.height(root.left)
        right_height = self.height(root.right)

        # Conquer step: 1 (current node) + maximum height of child branches
        return 1 + max(left_height, right_height)


# --- Driver Code and Verification ---
if __name__ == "__main__":
    """
    Constructing the example binary tree:
             1
            / \
           2   3
                \
                 4
    """
    # 1. Instantiate tree nodes
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.right.right = Node(4)

    # 2. Compute height
    solver = Solution()
    tree_height = solver.height(root)

    # 3. Print output
    print(f"Height of the binary tree: {tree_height}")