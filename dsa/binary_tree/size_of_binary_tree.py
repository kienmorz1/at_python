# Definition of a Binary Tree Node
class Node:
    def __init__(self, val: int):
        self.data = val
        self.left = None
        self.right = None


class Solution:
    def getSize(self, node: Node) -> int:
        # Base case: empty tree or leaf child pointer
        if node is None:
            return 0

        # Post-order calculation: 1 (current) + left subtree + right subtree
        return 1 + self.getSize(node.left) + self.getSize(node.right)


# --- Driver Code and Example Execution ---
if __name__ == "__main__":
    """
    Constructing the example binary tree:
             10
            /  \
           5    20
            \
             8
    """
    # 1. Create nodes
    root = Node(10)
    root.left = Node(5)
    root.right = Node(20)
    root.left.right = Node(8)

    # 2. Compute size
    solver = Solution()
    tree_size = solver.getSize(root)

    # 3. Print output
    print(f"Total size of the binary tree: {tree_size}")