# Procedure: Lowest Common Ancestor of a Binary Tree

This document describes how to locate the lowest common ancestor (LCA) of two given nodes in an arbitrary binary tree.

---

## 1. Technical Description

The **Lowest Common Ancestor (LCA)** between two nodes $p$ and $q$ is defined as the lowest node $T$ in tree that has both $p$ and $q$ as descendants (where a node can be a descendant of itself).
In an arbitrary binary tree, nodes are not sorted.
The procedure uses bottom-up recursion (post-order traversal) to search both branches and combine presence signals.

### Recursive Rules

1. **Base Condition:**
   - If `root is None`, return `None` (empty subtree contains neither node).
   - If `root == p` or `root == q`, return `root` (found one of the targets; propagate this node upwards).

2. **Recursive Step:**
   - Search the left subtree for $p$ or $q$.
   - Search the right subtree for $p$ or $q$.

3. **Conquer / Aggregation Rules:**
   - **Both branches return non-null (`left` and `right`):** The current node is the lowest split point where $p$ and $q$ diverge. Return `root`.
   - **Only one branch returns non-null:** Both nodes reside inside that single subtree (or one node was found deeper down). Propagate the non-null child reference.
   - **Both branches return null:** Neither target exists in this subtree. Return `None`.

---

## 2. Technical Justification with Examples

This section explains key engineering decisions and shows concrete failure points if alternate choices are made.

### Justification 1: Early Return on Matching Target vs Full Subtree Exploration

* **Reason:** When the current node matches $p$ (or $q$), you do not need to search beneath it immediately.
* **Positive Scenario ($p$ is an ancestor of $q$):**
  ```text
            [ 3 ] (Root)
           /
        [ 5 ] (Target p)
       /
    [ 4 ] (Target q)
  ```
  When recursion hits `Node(5)`, it returns `Node(5)` immediately without exploring `Node(4)`.
  If $q$ is below $p$, $p$ is by definition the LCA. If $q$ is elsewhere in another branch, the root will receive signals from both sides and choose the root. Returning early is always correct and saves operations.

---

### Justification 2: Bottom-Up Propagation vs Parent Pointers with Hash Sets

* **Reason:** Solving LCA using parent pointers requires storing every node's parent reference in a hash table or hash set, adding $\mathcal{O}(N)$ auxiliary memory overhead.
* **Failure Scenario (Memory Overhead):**
  Constructing a complete parent map for a tree with $10^5$ nodes allocates significant extra heap storage. Pure post-order recursion resolves the ancestor during stack unwinding in $\mathcal{O}(H)$ stack space without modifying nodes or allocating auxiliary hash maps.

---

### Justification 3: Handling Node Divergence (The Split Point)

* **Reason:** The LCA is uniquely identified as the node where one target is in its left branch and the other is in its right branch.
* **Example:**
  ```text
            [ 3 ]  <-- left returns Node(5), right returns Node(1)
           /     \
        [ 5 ]   [ 1 ]
  ```
  At `Node(3)`, `left` is `Node(5)` and `right` is `Node(1)`. Because both are non-null, `Node(3)` correctly identifies itself as the LCA and returns itself up the call chain.

---

## 3. Complete Python 3 Code Implementation

```python
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int = 0):
        self.val = val
        self.left: Optional['TreeNode'] = None
        self.right: Optional['TreeNode'] = None


class Solution:
    def lowestCommonAncestor(
        self, root: Optional[TreeNode], p: TreeNode, q: TreeNode
    ) -> Optional[TreeNode]:
        """
        Finds the Lowest Common Ancestor of two nodes in a binary tree.
        """
        # Base condition: empty branch or target node found
        if root is None or root == p or root == q:
            return root

        # Divide step: search left and right subtrees
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # Conquer step:
        # Case 1: p and q are in different subtrees, current node is the LCA
        if left is not None and right is not None:
            return root

        # Case 2: both nodes are in the left or right subtree (or only one was found)
        return left if left is not None else right


# --- Driver Code and Verification ---
if __name__ == "__main__":
    """
    Constructing the example binary tree:
             3
           /   \
          5     1
         / \   / \
        6   2 0   8
           / \
          7   4
    """
    # 1. Instantiate tree nodes
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)

    # 2. Assign targets
    target_p = root.left        # Node(5)
    target_q = root.right       # Node(1)
    target_q2 = root.left.right.right  # Node(4)

    solver = Solution()

    # Case A: Targets in different subtrees (5 and 1)
    lca_a = solver.lowestCommonAncestor(root, target_p, target_q)

    # Case B: One target is ancestor of the other (5 and 4)
    lca_b = solver.lowestCommonAncestor(root, target_p, target_q2)

    # 3. Print outputs
    print(f"LCA of Node(5) and Node(1): {lca_a.val if lca_a else None}")
    print(f"LCA of Node(5) and Node(4): {lca_b.val if lca_b else None}")
```

### Execution Output

```text
LCA of Node(5) and Node(1): 3
LCA of Node(5) and Node(4): 5
```

---

## 4. Complexity Data

- **Execution Time:** $\mathcal{O}(N)$
  - In the worst case, every node in the binary tree is inspected once.
  - $N$ is the total count of nodes in the binary tree.

- **Memory Usage:** $\mathcal{O}(H)$
  - Memory consumption corresponds to call stack frames proportional to tree height $H$.
  - $\mathcal{O}(\log N)$ for a balanced tree; $\mathcal{O}(N)$ for a skewed tree.

---

## 5. Execution Trace

### Example Input Tree

```text
         [3]
        /   \
      [5]   [1]
      / \
    [6] [2]
```

**Targets:** `p = Node(6)`, `q = Node(2)`

### Trace Table: Find Lowest Common Ancestor

| Step | Current Node | Sub-Operation | Returned Value | Status |
| :--- | :--- | :--- | :--- | :--- |
| 1 | `TreeNode(3)` | Call `lowestCommonAncestor(3, 6, 2)` | Pending | Waits for `Node(5)` and `Node(1)` |
| 2 | `TreeNode(5)` | Call `lowestCommonAncestor(5, 6, 2)` | Pending | Waits for `Node(6)` and `Node(2)` |
| 3 | `TreeNode(6)` | Base check: `root == p` | `Node(6)` | Resolves |
| 4 | `TreeNode(2)` | Base check: `root == q` | `Node(2)` | Resolves |
| 5 | `TreeNode(5)` | Both `left` and `right` are non-null | `Node(5)` | Resolves (LCA found at 5) |
| 6 | `TreeNode(1)` | Call `lowestCommonAncestor(1, 6, 2)` | Pending | Searches beneath `Node(1)` |
| 7 | `TreeNode(1)` | Subtrees return `None` | `None` | Resolves |
| 8 | `TreeNode(3)` | `left = Node(5)`, `right = None` | **`Node(5)`** | **Final LCA** |