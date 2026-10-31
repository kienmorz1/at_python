# Procedure: Calculate the Sum of Elements in a Binary Tree

This document describes how to calculate the sum of all node values stored in an arbitrary binary tree.

---

## 1. Technical Description

The sum of a binary tree is the aggregate arithmetic addition of data values from all nodes in the tree.
The procedure traverses each subtree recursively and combines the returned sums in a bottom-up direction.

### Recursive Rules

1. **Base Condition (Empty Tree or Leaf Child Pointer):**
   - When a node pointer is empty (`node is None`), return `0`.

2. **Recursive Step (Valid Node):**
   - Recursively compute the sum of all elements in the left subtree.
   - Recursively compute the sum of all elements in the right subtree.
   - Add the current node's value (`node.data`) to the left sum and the right sum.
   - Return the resulting sum.

---

## 2. Technical Justification with Examples

This section explains key engineering decisions and shows concrete failure points if alternate choices are made.

### Justification 1: Post-Order Aggregation vs Global Accumulators

* **Reason:** Pure functional recursion eliminates mutable global state, ensuring thread safety and preventing cross-call state corruption.
* **Positive Scenario:**
  ```text
            [ 10 ]
           /      \
        [ 20 ]   [ 30 ]
  ```
  `Node(10)` pauses its calculation until `Node(20)` returns `20` and `Node(30)` returns `30`.
  $$\text{Total} = 10 + 20 + 30 = 60$$
* **Failure Scenario (Global Mutable State):**
  Using a shared accumulator variable without reinitialization causes subsequent test executions to produce incorrect sums:
  ```python
  # Dangerous global pattern:
  total_sum = 0
  def badSum(root):
      global total_sum
      if not root: return
      total_sum += root.data
      badSum(root.left)
      badSum(root.right)
      return total_sum
  ```
  If `badSum` runs on Tree A (sum = 60) and then immediately on Tree B (sum = 25), Tree B outputs `85` instead of `25`. Pure bottom-up return values avoid this bug entirely.

---

### Justification 2: Base Return Value (`0`) vs Alternative Defaults

* **Reason:** Zero (`0`) is the additive identity in arithmetic. For any value $x$, $x + 0 = x$.
* **Failure Scenario:**
  If an empty leaf pointer returns anything other than `0` (e.g., `None` or `-1`):
  ```python
  # Wrong implementation:
  if node is None:
      return None
  ```
  Executing `node.data + left_sum + right_sum` attempts `int + NoneType`, raising a fatal runtime `TypeError: unsupported operand type(s) for +`.

---

### Justification 3: Exhaustive Traversal Requirement ($\mathcal{O}(N)$)

* **Reason:** An arbitrary binary tree maintains no value ordering invariant. Values (positive, negative, or zero) can reside at any leaf or branch depth.
* **Failure Scenario (Early Stopping Assumption):**
  If an algorithm stops searching a subtree when it encounters a `0` node:
  ```text
            [ 5 ]
           /
        [ 0 ]   <-- Early cutoff here drops downstream elements!
       /
    [ 50 ]
  ```
  Stopping early skips the descendant value `50`, producing an incorrect total of `5` instead of `55`. Every node must be visited.

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
```

### Execution Output

```text
Total sum of all nodes in binary tree: 43
```

---

## 4. Complexity Data

- **Execution Time:** $\mathcal{O}(N)$
  - Each node is visited exactly once during the traversal.
  - $N$ is the total count of nodes in the binary tree.

- **Memory Usage:** $\mathcal{O}(H)$
  - Call stack memory usage is proportional to tree height $H$.
  - $\mathcal{O}(\log N)$ for a balanced tree; $\mathcal{O}(N)$ for a skewed tree.

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

### Trace Table: Calculate Sum

| Step | Current Node | Sub-Operation | Returned Value | Status |
| :--- | :--- | :--- | :--- | :--- |
| 1 | `Node(10)` | Call `sumBT(10)` | Pending | Waits for `Node(5)` and `Node(20)` |
| 2 | `Node(5)` | Call `sumBT(5)` | Pending | Waits for left child and `Node(8)` |
| 3 | `None` (left of 5) | Base condition | `0` | Resolves |
| 4 | `Node(8)` (right of 5) | Call `sumBT(8)` | Pending | Waits for both child pointers |
| 5 | `None` (left of 8) | Base condition | `0` | Resolves |
| 6 | `None` (right of 8) | Base condition | `0` | Resolves |
| 7 | `Node(8)` | `8 + 0 + 0` | `8` | Resolves |
| 8 | `Node(5)` | `5 + 0 + 8` | `13` | Resolves |
| 9 | `Node(20)` (right of 10)| Call `sumBT(20)` | Pending | Waits for both child pointers |
| 10 | `None` (left of 20) | Base condition | `0` | Resolves |
| 11 | `None` (right of 20) | Base condition | `0` | Resolves |
| 12 | `Node(20)` | `20 + 0 + 0` | `20` | Resolves |
| 13 | `Node(10)` | `10 + 13 + 20` | **`43`** | **Final Sum** |