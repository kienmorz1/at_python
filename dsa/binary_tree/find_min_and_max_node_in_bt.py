class Node:
    def __init__(self, val: int):
        self.data = val
        self.left = None
        self.right = None


class Solution:
    def findMax(self, root: Node) -> int:
        """
        Returns the maximum value in the binary tree.
        """
        # Base condition: empty node returns the identity value for max
        if root is None:
            return float('-inf')

        # Divide step: recursively find max in both subtrees
        left_max = self.findMax(root.left)
        right_max = self.findMax(root.right)

        # Conquer step: aggregate current node with subtree maximums
        return max(root.data, left_max, right_max)

    def findMin(self, root: Node) -> int:
        """
        Returns the minimum value in the binary tree.
        """
        # Base condition: empty node returns the identity value for min
        if root is None:
            return float('inf')

        # Divide step: recursively find min in both subtrees
        left_min = self.findMin(root.left)
        right_min = self.findMin(root.right)

        # Conquer step: aggregate current node with subtree minimums
        return min(root.data, left_min, right_min)


# --- Driver Code and Verification ---
if __name__ == "__main__":
    """
    Constructing the example binary tree:
             10
            /  \
           5    20
            \
             8
    """
    # 1. Instantiate tree nodes
    root = Node(10)
    root.left = Node(5)
    root.right = Node(20)
    root.left.right = Node(8)

    # 2. Compute minimum and maximum
    solver = Solution()
    max_val = solver.findMax(root)
    min_val = solver.findMin(root)

    # 3. Print output
    print(f"Maximum value in binary tree: {max_val}")
    print(f"Minimum value in binary tree: {min_val}")