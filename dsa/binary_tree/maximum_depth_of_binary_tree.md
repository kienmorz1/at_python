# Procedure: Find Maximum Depth of Binary Tree

This document describes how to compute the maximum depth (height in terms of nodes) of a binary tree.

---

## 1. Technical Description

The maximum depth of a binary tree is the number of nodes along the longest path from the root node down to the farthest leaf node.
The procedure uses recursive divide-and-conquer to determine the depth of each child branch and selects the deeper path.

### Recursive Rules

1. **Base Condition (Empty Tree or Leaf Child Pointer):**
   - When a node pointer is empty (`root is None`), return `0`.

2. **Recursive Step (Valid Node):**
   - Recursively compute the maximum depth of the left subtree.
   - Recursively compute the maximum depth of the right subtree.
   - Take the maximum of both subtree depths and add `1` for the current node.
   - Return the resulting depth.

---

## 2. Technical Justification with Examples

This section explains key engineering decisions and shows concrete failure points if alternate choices are made.

### Justification 1: Taking `max()` of Subtrees vs Adding Both

* **Reason:** Depth measures a single path length, not the total node count.
* **Positive Scenario:**
  ```text
            [ 3 ]
           /     \
        [ 9 ]   [ 20 ]
                /    \
              [ 15 ] [ 7 ]
  ```
  `Node(3)` must select the deeper of its two branches:
  $$\text{Depth} = 1 + \max(\text{left\_depth}, \text{right\_depth}) = 1 + \max(1, 2) = 3$$
* **Failure Scenario (Summing Subtrees):**
  If an implementation adds subtree results instead of taking the maximum (`1 + left + right`), it computes the **size** (total nodes = 5) rather than the **depth** (longest path = 3).

---

### Justification 2: Base Return Value (`0`) vs Alternative Defaults

* **Reason:** An empty node contributes zero steps to the path length.
* **Failure Scenario (Returning `1` on `None`):**
  If the base case returns `1`:
  ```python
  # Wrong implementation:
  if root is None:
      return 1
  ```
  A tree with a single root node has two `None` children. The calculation becomes:
  $$1 + \max(1, 1) = 2$$
  The algorithm incorrectly reports a depth of `2` for a single-node tree (which actually has depth `1`).

---

### Justification 3: Exhaustive Exploration of Both Branches

* **Reason:** Binary trees do not guarantee balanced paths; the deepest leaf can reside on either side.
* **Failure Scenario (Assuming Left Branch is Deeper):**
  ```text
        [ 1 ]
       /     \
     [ 2 ]   [ 3 ]
                \
                [ 4 ]
                   \
                   [ 5 ]
  ```
  If traversal only inspects the left branch, it returns a depth of `2`. The true maximum depth is along the right branch (`4`). Every path must be evaluated.

---

## 3. Complete Python 3 Code Implementation

```python
from typing import Optional


# Definition for a binary tree node.
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
```

### Execution Output

```text
Maximum depth of the binary tree: 3
```

---

## 4. Complexity Data

- **Execution Time:** $\mathcal{O}(N)$
  - The procedure inspects every node exactly once.
  - $N$ is the total count of nodes in the binary tree.

- **Memory Usage:** $\mathcal{O}(H)$
  - Auxiliary memory represents call stack frames proportional to tree height $H$.
  - $\mathcal{O}(\log N)$ for a balanced tree; $\mathcal{O}(N)$ for a skewed tree.

---

## 5. Execution Trace

### Example Input Tree

```text
         [3]
        /   \
      [9]   [20]
            /  \
          [15] [7]
```

### Trace Table: Calculate Maximum Depth

| Step | Current Node | Sub-Operation | Returned Value | Status |
| :--- | :--- | :--- | :--- | :--- |
| 1 | `TreeNode(3)` | Call `maxDepth(3)` | Pending | Waits for `Node(9)` and `Node(20)` |
| 2 | `TreeNode(9)` | Call `maxDepth(9)` | Pending | Waits for left and right children |
| 3 | `None` (left of 9) | Base condition | `0` | Resolves |
| 4 | `None` (right of 9) | Base condition | `0` | Resolves |
| 5 | `TreeNode(9)` | `1 + max(0, 0)` | `1` | Resolves |
| 6 | `TreeNode(20)` (right of 3) | Call `maxDepth(20)` | Pending | Waits for `Node(15)` and `Node(7)` |
| 7 | `TreeNode(15)` (left of 20) | Call `maxDepth(15)` | Pending | Waits for left and right children |
| 8 | `None` (left of 15) | Base condition | `0` | Resolves |
| 9 | `None` (right of 15) | Base condition | `0` | Resolves |
| 10 | `TreeNode(15)` | `1 + max(0, 0)` | `1` | Resolves |
| 11 | `TreeNode(7)` (right of 20) | Call `maxDepth(7)` | Pending | Waits for left and right children |
| 12 | `None` (left of 7) | Base condition | `0` | Resolves |
| 13 | `None` (right of 7) | Base condition | `0` | Resolves |
| 14 | `TreeNode(7)` | `1 + max(0, 0)` | `1` | Resolves |
| 15 | `TreeNode(20)` | `1 + max(1, 1)` | `2` | Resolves |
| 16 | `TreeNode(3)` | `1 + max(1, 2)` | **`3`** | **Final Maximum Depth** |