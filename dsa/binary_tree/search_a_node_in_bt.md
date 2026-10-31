# Procedure: Search a Node in a Binary Search Tree (BST)

This document describes how to search for a target value in a Binary Search Tree.

---

## 1. Technical Description

A Binary Search Tree (BST) maintains an ordering invariant:
- All keys in the **left subtree** of a node are strictly smaller than the node's value.
- All keys in the **right subtree** of a node are strictly greater than the node's value.

Because of this property, a search operation does not inspect every node. 
At each step, the procedure compares the target value with the current node's value and discards half of the remaining tree.

### Recursive Rules

1. **Base Conditions:**
   - **Target Found:** If `root.data == key`, return `True` (or the node reference).
   - **Target Absent (Empty Subtree):** If `root is None`, return `False` (the key does not exist).

2. **Recursive Decisions:**
   - **Branch Left:** If `key < root.data`, search strictly inside the left subtree (`root.left`).
   - **Branch Right:** If `key > root.data`, search strictly inside the right subtree (`root.right`).

---

## 2. Technical Justification with Examples

This section explains why each design decision is necessary and shows concrete failure points if alternate choices are made.

### Justification 1: Pruning Subtrees via BST Invariant vs Linear Traversal

* **Reason:** In a valid BST, the ordering property guarantees that a target smaller than the current node cannot exist anywhere in the right subtree (and vice versa).
* **Positive Scenario:**
  ```text
            [ 20 ]
           /      \
        [ 10 ]   [ 30 ]
       /     \
     [ 5 ]  [ 15 ]
  ```
  If searching for `key = 15`:
  - At `Node(20)`: $15 < 20 \implies$ Entire right subtree (`[30]`) is discarded immediately.
  - At `Node(10)`: $15 > 10 \implies$ Entire left subtree (`[5]`) is discarded immediately.
  - At `Node(15)`: Target found in 3 steps instead of 5.
* **Failure Scenario (Ignoring Ordering and Searching Both Branches):**
  If an implementation searches both branches unconditionally:
  ```python
  # Inefficient implementation:
  return self.search(root.left, key) or self.search(root.right, key)
  ```
  This degrades performance from $\mathcal{O}(\log N)$ on balanced trees down to $\mathcal{O}(N)$, destroying the primary performance advantage of a BST.

---

### Justification 2: Base Return Value (`False` / `None`) on Empty Node

* **Reason:** Reaching `None` indicates the traversal followed the exact directional path where the value should exist according to the invariant, but hit a leaf termination.
* **Failure Scenario (Looping or Unhandled `None`):**
  If the base case does not check for `root is None` before accessing `root.data`:
  ```python
  # Wrong implementation:
  if root.data == key:  # Raises AttributeError if root is None
      return True
  ```
  Searching for a non-existent key leads to an unhandled exception when reaching a leaf's child pointer.

---

### Justification 3: Recursive vs Iterative Equivalence

* **Reason:** Search in a BST is a **tail-recursive** operation: only one path is followed, and no post-processing computation is performed when calls return.
* **Impact:** Both recursive and iterative solutions run in $\mathcal{O}(H)$ time, but an iterative `while` loop operates in $\mathcal{O}(1)$ auxiliary space without stack overhead.

---

## 3. Complete Python 3 Code Implementation

```python
# Definition of a BST Node
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
```

### Execution Output

```text
Key 15 found in BST: True
Key 25 found in BST: False
```

---

## 4. Complexity Data

- **Execution Time:**
  - **Balanced BST (Average Case):** $\mathcal{O}(\log N)$ — each step halves the remaining search space.
  - **Skewed BST (Worst Case):** $\mathcal{O}(H) = \mathcal{O}(N)$ — tree degrades into a linked list structure.

- **Memory Usage:**
  - **Recursive Implementation:** $\mathcal{O}(H)$ call stack depth ($\mathcal{O}(\log N)$ balanced, $\mathcal{O}(N)$ skewed).
  - **Iterative Implementation:** $\mathcal{O}(1)$ constant auxiliary memory.

---

## 5. Execution Trace

### Example Input BST

```text
         [20]
        /    \
      [10]   [30]
      /  \
    [5]  [15]
```

### Trace Table: Search for `key = 15` (Success Case)

| Step | Current Node | Condition Evaluated | Decision | Returned Value | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `Node(20)` | `15 < 20` | Branch Left | Pending | Calls `search(10, 15)` |
| 2 | `Node(10)` | `15 > 10` | Branch Right | Pending | Calls `search(15, 15)` |
| 3 | `Node(15)` | `15 == 15` | Target Found | `True` | Resolves |
| 4 | `Node(10)` | Left call resolved | Return child result | `True` | Resolves |
| 5 | `Node(20)` | Right call resolved | Return child result | **`True`** | **Final Result** |

### Trace Table: Search for `key = 25` (Failure Case)

| Step | Current Node | Condition Evaluated | Decision | Returned Value | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `Node(20)` | `25 > 20` | Branch Right | Pending | Calls `search(30, 25)` |
| 2 | `Node(30)` | `25 < 30` | Branch Left | Pending | Calls `search(None, 25)` |
| 3 | `None` (left of 30) | `root is None` | Base Condition | `False` | Resolves |
| 4 | `Node(30)` | Left call resolved | Return child result | `False` | Resolves |
| 5 | `Node(20)` | Right call resolved | Return child result | **`False`** | **Final Result** |