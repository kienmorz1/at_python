# Procedure: Path to Given Node in a Binary Tree

This document describes how to find the root-to-node path for a target value in a binary tree.

---

## 1. Technical Description

Given the root of a binary tree and a target value $B$, the goal is to return a sequence of node values starting at the root and ending at node $B$.
Because the binary tree has no sorted order, the procedure uses depth-first backtracking to explore branches, record candidate nodes, and remove dead-end paths.

### Recursive Rules

1. **Base Condition (Empty Tree or Null Child):**
   - If `root is None`, return `False` (target not found along this branch).

2. **Exploration Step:**
   - Append the current node's value (`root.val`) to the path list.
   - If `root.val == B`, return `True` (target found).

3. **Branching Step:**
   - Recursively search the left subtree. If it returns `True`, return `True`.
   - Recursively search the right subtree. If it returns `True`, return `True`.

4. **Backtracking Step (Dead End):**
   - If neither child branch contains target $B$, remove (`pop`) the current node value from the path list.
   - Return `False` to the caller.

---

## 2. Technical Justification with Examples

This section explains key engineering decisions and shows concrete failure points if alternate choices are made.

### Justification 1: In-Place Backtracking vs Path Copying

* **Reason:** Copying path lists at every recursion level creates substantial memory and time overhead.
* **Positive Scenario:**
  By maintaining a single dynamic array and popping dead ends upon retreat:
  ```python
  path.append(root.val)
  if search(left) or search(right):
      return True
  path.pop()  # Backtrack in O(1)
  ```
  Only nodes on the active recursion stack reside in memory, keeping auxiliary space bounded by tree height $\mathcal{O}(H)$.
* **Failure Scenario (Path Concatenation per Call):**
  Doing `current_path + [root.val]` duplicates array slices of length up to $N$ across $N$ function frames, inflating time complexity to $\mathcal{O}(N^2)$ and consuming unnecessary heap memory.

---

### Justification 2: Early Termination on Target Discovery

* **Reason:** Once target $B$ is found, the current state of the path array is the final answer.
* **Positive Scenario:**
  ```text
            [ 1 ]
           /     \
        [ 2 ]   [ 3 ]
       /
     [ 4 ]  <-- Target B = 4
  ```
  When `Node(4)` matches, it returns `True` immediately. `Node(2)` and `Node(1)` detect `True` and skip traversing their other child branches (such as `Node(3)`), avoiding unnecessary work.

---

### Justification 3: Safe Node Removal During Backtracking

* **Reason:** If a node's left and right subtrees both fail to locate $B$, that node cannot be part of the valid route.
* **Failure Scenario (Missing Backtrack Step):**
  If `path.pop()` is omitted:
  ```text
            [ 1 ]
           /     \
        [ 2 ]   [ 3 ]  <-- Target B = 3
  ```
  The search tests `Node(1) -> Node(2)` first. Without popping `Node(2)` after it fails, the returned path becomes `[1, 2, 3]` instead of `[1, 3]`.

---

## 3. Complete Python 3 Code Implementation

```python
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x: int):
        self.val = x
        self.left: Optional['TreeNode'] = None
        self.right: Optional['TreeNode'] = None


class Solution:
    def solve(self, A: Optional[TreeNode], B: int) -> List[int]:
        """
        Finds the path from the root node to the node with value B.
        """
        path: List[int] = []

        def findPath(node: Optional[TreeNode], target: int) -> bool:
            # Base condition: empty node branch hit
            if node is None:
                return False

            # Add current node to candidate path
            path.append(node.val)

            # Target found
            if node.val == target:
                return True

            # Explore child branches
            if findPath(node.left, target) or findPath(node.right, target):
                return True

            # Backtrack: target is not present in subtrees of this node
            path.pop()
            return False

        findPath(A, B)
        return path


# --- Driver Code and Verification ---
if __name__ == "__main__":
    """
    Constructing the example binary tree:
             1
           /   \
          2     3
         / \   / \
        4   5 6   7
    """
    # 1. Instantiate tree nodes
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    # 2. Search for path to target node 5
    solver = Solution()
    target = 5
    result_path = solver.solve(root, target)

    # 3. Print output
    print(f"Path to node {target}: {result_path}")
```

### Execution Output

```text
Path to node 5: [1, 2, 5]
```

---

## 4. Complexity Data

- **Execution Time:** $\mathcal{O}(N)$
  - Each node is visited at most once during traversal.
  - $N$ is the total count of nodes in the binary tree.

- **Memory Usage:** $\mathcal{O}(H)$
  - Call stack frames and the `path` array grow proportionally to tree height $H$.
  - $\mathcal{O}(\log N)$ for a balanced tree; $\mathcal{O}(N)$ for a skewed tree.

---

## 5. Execution Trace

### Example Input Tree

```text
         [1]
        /   \
      [2]   [3]
      / \
    [4] [5]
```

**Target:** `B = 5`

### Trace Table: Find Path to Node `5`

| Step | Current Node | Path Array Before Step | Action / Condition | Path Array After Step | Returned Value | Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `TreeNode(1)` | `[]` | Append `1`; explore left | `[1]` | Pending | Calls `findPath(2)` |
| 2 | `TreeNode(2)` | `[1]` | Append `2`; explore left | `[1, 2]` | Pending | Calls `findPath(4)` |
| 3 | `TreeNode(4)` | `[1, 2]` | Append `4`; `4 != 5`; explore left | `[1, 2, 4]` | Pending | Calls `findPath(None)` |
| 4 | `None` (left of 4) | `[1, 2, 4]` | Base condition | `[1, 2, 4]` | `False` | Resolves |
| 5 | `TreeNode(4)` | `[1, 2, 4]` | Explore right | `[1, 2, 4]` | Pending | Calls `findPath(None)` |
| 6 | `None` (right of 4) | `[1, 2, 4]` | Base condition | `[1, 2, 4]` | `False` | Resolves |
| 7 | `TreeNode(4)` | `[1, 2, 4]` | Both subtrees `False` $\rightarrow$ pop `4` | `[1, 2]` | `False` | Resolves (Back)