# Procedure: Find Maximum and Minimum Elements in a Binary Tree

This document describes how to find the maximum and minimum values in an unordered binary tree.

---

## 1. Technical Description

An unordered binary tree does not sort data. 
You must examine every node to find the extreme values.

### Recursive Rules

1. **Base Condition (No Node):**
   - When you search for the maximum value, return negative infinity (`-inf`).
   - When you search for the minimum value, return positive infinity (`+inf`).

2. **Search Condition (Valid Node):**
   - Read the value from the current node.
   - Run the search on the left child node.
   - Run the search on the right child node.
   - Compare the three values and return the result.

---

## 2. Technical Justification with Examples

This section explains key engineering decisions and shows concrete failure points if alternate choices are made.

### Justification 1: Exhaustive Traversal vs BST Pruning

* **Reason:** An arbitrary binary tree enforces no ordering rules between parents and children.
* **Positive Scenario (Binary Search Tree):** If the tree were an ordered BST, the maximum value would reside exclusively along right-child pointers ($\mathcal{O}(H)$ time).
* **Failure Scenario (Arbitrary Binary Tree):**
  ```text
            [ 50 ]
           /      \
        [ 20 ]   [ 30 ]
        /
     [ 999 ]  <-- The absolute maximum is hidden deep in the left subtree!
  ```
  If traversal skips the left branch based on root comparisons, the algorithm returns `50` instead of `999`. Therefore, visiting all $N$ nodes is mandatory.

---

### Justification 2: Base Values (`-inf` / `+inf`) vs Fallback Defaults (`0`)

* **Reason:** The neutral base value must not overwrite any real node data during `max()` or `min()` comparisons.
* **Failure Scenario with Default `0` for `findMax`:**
  Consider a tree that contains only negative numbers:
  ```text
            [ -15 ]
           /       \
       [ -30 ]    [ -5 ]
  ```
  If an empty branch returns `0` instead of `-inf`:
  ```python
  # Wrong implementation:
  left_max = 0
  right_max = 0
  result = max(-5, 0, 0) # evaluates to 0
  ```
  The algorithm outputs `0` as the maximum value. Because `0` is not present in the tree, this output is mathematically incorrect. Using `-inf` guarantees that $\max(x, -\infty) = x$ for any real number $x$.

* **Failure Scenario with Default `0` for `findMin`:**
  Consider a tree that contains only positive numbers:
  ```text
            [ 15 ]
           /      \
        [ 30 ]    [ 5 ]
  ```
  If an empty branch returns `0` instead of `+inf`:
  ```python
  # Wrong implementation:
  left_min = 0
  right_min = 0
  result = min(5, 0, 0) # evaluates to 0
  ```
  The algorithm outputs `0` instead of `5`. Using `+inf` guarantees that $\min(x, +\infty) = x$ for any real number $x$.

---

### Justification 3: Bottom-Up Post-Order vs Top-Down State Passing

* **Reason:** A node cannot declare itself as the extremum of its subtree until both its left and right descendants provide their values.
* **Example:**
  ```text
            [ 10 ]
           /      \
        [ 25 ]   [ 12 ]
  ```
  `Node(10)` cannot compute its local maximum before `Node(25)` and `Node(12)` report back. Post-order traversal guarantees that leaf nodes resolve first, propagating only the optimal values up the tree to the caller.

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
```

### Execution Output

```text
Maximum value in binary tree: 20
Minimum value in binary tree: 5
```

---

## 4. Complexity Data

- **Execution Time:** $\mathcal{O}(N)$
  - The procedure reads each node one time.
  - $N$ is the total count of nodes in the binary tree.

- **Memory Usage:** $\mathcal{O}(H)$
  - Memory consumption corresponds to the maximum depth of the call stack.
  - $H$ is the tree height ($\mathcal{O}(\log N)$ for a balanced tree; $\mathcal{O}(N)$ for a skewed tree).

---

## 5. Execution Trace

### Example Input Tree

```text
         [10]
        /    \
      [5]    [20]
        \
        [8]
```

### Trace Table: Find Maximum Value

| Step | Current Node | Sub-Operation | Returned Value | Status |
| :--- | :--- | :--- | :--- | :--- |
| 1 | `Node(10)` | Start search | Pending | Waits for left branch |
| 2 | `Node(5)` | Start search | Pending | Waits for left branch |
| 3 | `None` (left of 5) | Base condition | `-inf` | Resolves |
| 4 | `Node(8)` (right of 5) | Start search | Pending | Waits for child branches |
| 5 | `None` (left of 8) | Base condition | `-inf` | Resolves |
| 6 | `None` (right of 8) | Base condition | `-inf` | Resolves |
| 7 | `Node(8)` | `max(8, -inf, -inf)` | `8` | Resolves |
| 8 | `Node(5)` | `max(5, -inf, 8)` | `8` | Resolves |
| 9 | `Node(20)` (right of 10)| `max(20, -inf, -inf)`| `20` | Resolves |
| 10 | `Node(10)` | `max(10, 8, 20)` | **`20`** | **Final Maximum** |

### Trace Table: Find Minimum Value

| Step | Current Node | Sub-Operation | Returned Value | Status |
| :--- | :--- | :--- | :--- | :--- |
| 1 | `Node(10)` | Start search | Pending | Waits for left branch |
| 2 | `Node(5)` | Start search | Pending | Waits for left branch |
| 3 | `None` (left of 5) | Base condition | `+inf` | Resolves |
| 4 | `Node(8)` (right of 5) | Start search | Pending | Waits for child branches |
| 5 | `None` (left of 8) | Base condition | `+inf` | Resolves |
| 6 | `None` (right of 8) | Base condition | `+inf` | Resolves |
| 7 | `Node(8)` | `min(8, +inf, +inf)` | `8` | Resolves |
| 8 | `Node(5)` | `min(5, +inf, 8)` | `5` | Resolves |
| 9 | `Node(20)` (right of 10)| `min(20, +inf, +inf)`| `20` | Resolves |
| 10 | `Node(10)` | `min(10, 5, 20)` | **`5`** | **Final Minimum** |