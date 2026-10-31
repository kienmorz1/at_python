# Procedure: Calculate the Height of a Binary Tree

This document describes how to compute the height of a binary tree.

---

## 1. Technical Description

The height of a binary tree is defined as the number of edges (or levels/nodes, depending on convention) on the longest downward path from the root node to a leaf node. 
In GeeksforGeeks conventions, height is measured by the total count of **nodes** along the longest root-to-leaf path (equivalent to Maximum Depth).
The procedure computes the maximum height of child subtrees recursively and adds the current node.

### Recursive Rules

1. **Base Condition (Empty Tree or Leaf Child Pointer):**
   - When a node pointer is empty (`node is None`), return `0`.

2. **Recursive Step (Valid Node):**
   - Recursively calculate the height of the left subtree.
   - Recursively calculate the height of the right subtree.
   - Select the greater value between the left and right subtree heights.
   - Add `1` for the current node and return the result.

---

## 2. Technical Justification with Examples

This section explains key engineering decisions and shows concrete failure points if alternate choices are made.

### Justification 1: Comparing Subtree Heights via `max()` vs Summing

* **Reason:** Height measures the single longest branch from the current node down to a leaf, not the cumulative size of the subtrees.
* **Positive Scenario:**
  ```text
            [ 1 ]
           /     \
        [ 2 ]   [ 3 ]
                 /
               [ 4 ]
  ```
  `Node(1)` evaluates both child branches:
  $$\text{Left Height} = 1, \quad \text{Right Height} = 2$$
  $$\text{Height} = 1 + \max(1, 2) = 1 + 2 = 3$$
* **Failure Scenario (Summing Subtrees):**
  If an implementation adds both branch results (`1 + left + right`), it calculates the total node count (`4`) instead of the longest path length (`3`).

---

### Justification 2: Base Return Value (`0`) vs Omitting Base Check

* **Reason:** An empty branch has no nodes and contributes zero height to the path.
* **Failure Scenario (Returning `1` on `None`):**
  If `node is None` returns `1`:
  ```python
  # Wrong implementation:
  if node is None:
      return 1
  ```
  For a single root node with two `None` children:
  $$\text{Height} = 1 + \max(1, 1) = 2$$
  The calculation returns `2` for a single-node tree when the true node-based height is `1`.

---

### Justification 3: Exhaustive Traversal Requirement ($\mathcal{O}(N)$)

* **Reason:** In an unsorted binary tree, the longer path can exist on either the left or right branch at any depth.
* **Failure Scenario (Branch Greediness):**
  ```text
            [ 10 ]
           /      \
        [ 5 ]    [ 20 ]
        /           \
      [ 2 ]        [ 30 ]
                     \
                    [ 40 ]
  ```
  Stopping exploration after seeing the left branch has depth `2` without checking the right branch fails to identify that the right branch extends to depth `3`. Every node must be evaluated.

---

## 3. Complete Python 3 Code Implementation

```python
# Definition of a Binary Tree Node
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
```

### Execution Output

```text
Height of the binary tree: 3
```

---

## 4. Complexity Data

- **Execution Time:** $\mathcal{O}(N)$
  - The procedure inspects every node exactly once.
  - $N$ is the total count of nodes in the binary tree.

- **Memory Usage:** $\mathcal{O}(H)$
  - Auxiliary memory corresponds to the call stack frames proportional to tree height $H$.
  - $\mathcal{O}(\log N)$ for a balanced tree; $\mathcal{O}(N)$ for a skewed tree.

---

## 5. Execution Trace

### Example Input Tree

```text
         [1]
        /   \
      [2]   [3]
             \
             [4]
```

### Trace Table: Calculate Height

| Step | Current Node | Sub-Operation | Returned Value | Status |
| :--- | :--- | :--- | :--- | :--- |
| 1 | `Node(1)` | Call `height(1)` | Pending | Waits for `Node(2)` and `Node(3)` |
| 2 | `Node(2)` | Call `height(2)` | Pending | Waits for both child pointers |
| 3 | `None` (left of 2) | Base condition | `0` | Resolves |
| 4 | `None` (right of 2) | Base condition | `0` | Resolves |
| 5 | `Node(2)` | `1 + max(0, 0)` | `1` | Resolves |
| 6 | `Node(3)` (right of 1) | Call `height(3)` | Pending | Waits for left child and `Node(4)` |
| 7 | `None` (left of 3) | Base condition | `0` | Resolves |
| 8 | `Node(4)` (right of 3) | Call `height(4)` | Pending | Waits for both child pointers |
| 9 | `None` (left of 4) | Base condition | `0` | Resolves |
| 10 | `None` (right of 4) | Base condition | `0` | Resolves |
| 11 | `Node(4)` | `1 + max(0, 0)` | `1` | Resolves |
| 12 | `Node(3)` | `1 + max(0, 1)` | `2` | Resolves |
| 13 | `Node(1)` | `1 + max(1, 2)` | **`3`** | **Final Height** |