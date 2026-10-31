class Node:
    def __init__(self, val: int):
        self.data = val
        self.left = None
        self.right = None


class Solution:
    def sumBT(self, root: Node) -> int:
        """
        Calculates the sum of all elements in the binary tree.
        """
        # Base condition: an empty subtree contributes 0 to the sum
        if root is None:
            return 0

        # Divide step: recursively calculate sum of left and right subtrees
        left_sum = self.sumBT(root.left)
        right_sum = self.sumBT(root.right)

        # Conquer step: combine current node data with subtree sums
        return root.data + left_sum + right_sum


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

    # 2. Compute total sum
    solver = Solution()
    total = solver.sumBT(root)

    # 3. Print output
    print(f"Total sum of all nodes in binary tree: {total}")