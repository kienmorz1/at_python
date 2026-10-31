# Procedure: Calculate the Size of a Binary Tree

This document describes how to calculate the total number of nodes in a binary tree.

---

## 1. Technical Description

The size of a binary tree is the count of all nodes in that tree.
To find this count, the procedure traverses all branches recursively and aggregates the count bottom-up.

### Recursive Rules

1. **Base Condition (Empty Tree or Child):**
   - When a node pointer is empty (`node is None`), return `0`.

2. **Recursive Step (Valid Node):**
   - Calculate the size of the left subtree.
   - Calculate the size of the right subtree.
   - Add `1` for the current node to the sum of both subtrees.
   - Return the resulting total.

---

## 2. Technical Justification with Examples

This section explains the design choices and shows failure cases when incorrect logic is used.

### Justification 1: Post-Order Aggregation vs Pre-Order Accumulation

* **Reason:** A parent node cannot compute its own subtree size until both child branches have finished counting their nodes.
* **Positive Scenario:**
  ```text
            [ 1 ]
           /     \
        [ 2 ]   [ 3 ]
  ```
  `Node(1)` waits for `Node(2)` to return `1` and `Node(3)` to return `1`. Then it computes:
  $$\text{Total} = 1 + 1 + 1 = 3$$
  This removes the need for global state or mutable variables across function calls.

---

### Justification 2: Base Return Value (`0`) vs Omitting Base Check

* **Reason:** An empty branch contains zero nodes. In addition, the base case provides the termination signal for the recursion stack.
* **Failure Scenario (Missing or Incorrect Base Check):**
  If the base case returns `1` or does not check for `None`:
  ```python
  # Wrong implementation:
  if node is None:
      return 1  # Treats non-existent leaves as real nodes!
  ```
  For a single root node with two `None` children, this erroneous logic evaluates:
  $$\text{Size} = 1 + 1 + 1 = 3$$
  The program returns `3` for a tree with only 1 node. Returning `0` is mathematically required because the neutral element for addition is `0` ($x + 0 = x$).

---

### Justification 3: Visiting Every Node ($\mathcal{O}(N)$) vs Partial Traversal

* **Reason:** In an arbitrary binary tree, nodes are not placed in any specific balance or structure.
* **Failure Scenario (Assuming Balanced Height):**
  ```text
            [ 1 ]
           /
        [ 2 ]
       /
    [ 3 ]
  ```
  A programmer might try to compute size using height ($2^H - 1$). For this tree of height 3:
  $$2^3 - 1 = 7$$
  The real node count is `3`. Because skewed trees do not follow full-tree formulas, every node must be visited individually.

---

## 3. Python Code Implementation

```python
class Node:
    def __init__(self, val: int):
        self.data = val
        self.left = None
        self.right = None


class Solution:
    def getSize(self, node: Node) -> int:
        # Base condition: an empty branch has 0 nodes
        if node is None:
            return 0

        # Divide step: calculate size of both subtrees
        left_size = self.getSize(node.left)
        right_size = self.getSize(node.right)

        # Conquer step: aggregate current node (1) with subtree sizes
        return 1 + left_size + right_size
```

---

## 4. Complexity Data

- **Execution Time:** $\mathcal{O}(N)$
  - The procedure visits each node one time.
  - $N$ is the total count of nodes in the tree.

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

### Trace Table: Calculate Size

| Step | Current Node | Sub-Operation | Returned Value | Status |
| :--- | :--- | :--- | :--- | :--- |
| 1 | `Node(10)` | Call `getSize(10)` | Pending | Waits for `Node(5)` and `Node(20)` |
| 2 | `Node(5)` | Call `getSize(5)` | Pending | Waits for left child and `Node(8)` |
| 3 | `None` (left of 5) | Base condition | `0` | Resolves |
| 4 | `Node(8)` (right of 5) | Call `getSize(8)` | Pending | Waits for both child pointers |
| 5 | `None` (left of 8) | Base condition | `0` | Resolves |
| 6 | `None` (right of 8) | Base condition | `0` | Resolves |
| 7 | `Node(8)` | `1 + 0 + 0` | `1` | Resolves |
| 8 | `Node(5)` | `1 + 0 + 1` | `2` | Resolves |
| 9 | `Node(20)` (right of 10)| Call `getSize(20)` | Pending | Waits for both child pointers |
| 10 | `None` (left of 20) | Base condition | `0` | Resolves |
| 11 | `None` (right of 20) | Base condition | `0` | Resolves |
| 12 | `Node(20)` | `1 + 0 + 0` | `1` | Resolves |
| 13 | `Node(10)` | `1 + 2 + 1` | **`4`** | **Final Size** |