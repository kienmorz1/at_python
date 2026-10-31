class Node:
    def __init__(self, val: int):
        self.data = val
        self.left = None
        self.right = None


class Solution:
    def search(self, root: Node, key: int) -> bool:
        """
        Searches for a key in a Binary Search Tree (BST).
        Returns True if found, otherwise False.
        """
        # Base condition: empty branch hit (key does not exist)
        if root is None:
            return False

        # Target found
        if root.data == key:
            return True

        # BST invariant: target is smaller, search left branch
        if key < root.data:
            return self.search(root.left, key)

        # BST invariant: target is larger, search right branch
        return self.search(root.right, key)

    def searchIterative(self, root: Node, key: int) -> bool:
        """
        Iterative variant utilizing O(1) auxiliary space.
        """
        curr = root
        while curr is not None:
            if curr.data == key:
                return True
            elif key < curr.data:
                curr = curr.left
            else:
                curr = curr.right
        return False


# --- Driver Code and Verification ---
if __name__ == "__main__":
    """
    Constructing the example BST:
             20
            /  \
           10   30
          /  \
         5    15
    """
    # 1. Instantiate tree nodes
    root = Node(20)
    root.left = Node(10)
    root.right = Node(30)
    root.left.left = Node(5)
    root.left.right = Node(15)

    # 2. Search for existing and non-existing keys
    solver = Solution()
    found_15 = solver.search(root, 15)
    found_25 = solver.search(root, 25)

    # 3. Print output
    print(f"Key 15 found in BST: {found_15}")
    print(f"Key 25 found in BST: {found_25}")