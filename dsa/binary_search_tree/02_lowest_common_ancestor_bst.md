# 02 — Lowest Common Ancestor of a BST (LeetCode 235)

**Link:** https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

## Problem
Given a BST and two nodes `p`, `q`, return the lowest node that has both as descendants (a node counts as its own descendant).

Example: `root = [6,2,8,0,4,7,9,null,null,3,5]`, `p = 2`, `q = 8` → `6`.
`p = 2`, `q = 4` → `2` (2 is an ancestor of 4).

## Approach
Use the BST ordering to decide direction, the same way as search:
- If **both** `p.val` and `q.val` are smaller than `cur.val`, both live in the left subtree → move left.
- If **both** are larger → move right.
- Otherwise they **split** here (one on each side), or one of them **equals** `cur` → `cur` is the LCA.

No need for a general-tree LCA with parent pointers or path lists; the BST order gives the answer directly.

## Pattern to remember
> **LCA in BST = the first node that falls *between* p and q (inclusive).** Walk down until `min(p,q) <= cur <= max(p,q)`.

## Complexity
- Time: O(h)
- Space: O(h) for the recursion stack (O(1) if written iteratively)

## Dry run
`root = [6,2,8,0,4,7,9,null,null,3,5]`, `p = 2`, `q = 8`

| Step | cur | Check | Decision |
|------|-----|-------|----------|
| 1 | 6 | p=2<6 and q=8>6 → split | return 6 |

`p = 2`, `q = 4`:

| Step | cur | Check | Decision |
|------|-----|-------|----------|
| 1 | 6 | 2<6 and 4<6 → both left | cur = 2 |
| 2 | 2 | 2 == p (not < or >, so else branch) | return 2 |

## Common mistakes
- Comparing `p` and `q` *node objects* instead of `.val`.
- Using the generic binary tree LCA (which searches both sides) — slower and unnecessary here.

## Approach 1 — Recursive (submitted solution)
Recurse into the side that holds both nodes. Return the current node when they split or when it equals one of them.

```python
def lowestCommonAncestor(self, root, p, q):
    if root is None:
        return None
    if root.val > p.val and root.val > q.val:
        return self.lowestCommonAncestor(root.left, p, q)
    if root.val < p.val and root.val < q.val:
        return self.lowestCommonAncestor(root.right, p, q)
    return root
```

Dry run for `root = [6,2,8,0,4,7,9,null,null,3,5]`, `p = 2`, `q = 4`:
- `LCA(6)`: 2 < 6 and 4 < 6 → `LCA(2)`.
- `LCA(2)`: neither branch matches (p equals 2) → return 2.

## Approach 2 — Iterative (alternative)
Same decisions, with a loop. Space is O(1).

```python
def lowestCommonAncestor(root, p, q):
    cur = root
    while cur:
        if p.val < cur.val and q.val < cur.val:
            cur = cur.left
        elif p.val > cur.val and q.val > cur.val:
            cur = cur.right
        else:
            return cur
    return None
```

Both approaches follow the same path. The recursive one returns through the call stack, and the iterative one returns from the loop.

## Full program (`02_lowest_common_ancestor_bst.py`)

```python
"""LeetCode 235 - Lowest Common Ancestor of a Binary Search Tree (recursive solution).

Given a BST and two nodes p and q (both exist in the tree), return their lowest common ancestor.
A node may be an ancestor of itself.
"""
from tree_utils import TreeNode, build_tree


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return root


if __name__ == "__main__":
    sol = Solution()
    root = build_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    p = TreeNode(2)  # compared by value only
    q = TreeNode(8)
    print(sol.lowestCommonAncestor(root, p, q).val)  # 6

    node2 = root.left         # value 2
    node4 = root.left.right   # value 4
    print(sol.lowestCommonAncestor(root, node2, node4).val)  # 2
    assert sol.lowestCommonAncestor(root, p, q).val == 6
    assert sol.lowestCommonAncestor(root, node2, node4).val == 2
    print("all checks passed")
```
