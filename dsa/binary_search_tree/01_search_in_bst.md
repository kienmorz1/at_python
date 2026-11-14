# 01 — Search in a Binary Search Tree (LeetCode 700)

**Link:** https://leetcode.com/problems/search-in-a-binary-search-tree/

## Problem
Given `root` of a BST and an integer `val`, return the subtree rooted at the node whose value is `val`. Return `None` if not found.

Example: `root = [4,2,7,1,3]`, `val = 2` → `[2,1,3]`

## Approach
Use the BST ordering: at each node, compare `val` with `node.val`.
- `val < node.val` → the target can only be in the left subtree.
- `val > node.val` → only in the right subtree.
- equal → found.

Each comparison throws away one whole subtree, so we only ever walk a single root-to-leaf path.

## Pattern to remember
> **BST search = binary search on a path.** Compare, pick a side, repeat.

## Complexity
- Time: O(h) — h is the height. O(log n) if balanced, O(n) if skewed.
- Space: O(h) for the recursion stack (O(1) if written iteratively).

## Dry run
`root = [4,2,7,1,3]`, `val = 2`

| Step | root | root.val | Compare | Move |
|------|------|----------|---------|------|
| 1 | 4 | 4 | 2 < 4 | go left → 2 |
| 2 | 2 | 2 | 2 == 2 | loop stops |

Return node `2` → its subtree `[2,1,3]`.

For `val = 5`: 4 → right (7) → 5 < 7 → left (None). Loop exits with `None`.

## Common mistakes
- Forgetting `root and` in the loop condition → crash on `None`.
- Searching both sides (plain DFS) — wastes time and ignores the BST property.

## Approach 1 — Recursive (submitted solution)
Same idea, one call per node on the path. The recursion returns the found node up the stack.

```python
def searchBST(self, root, key):
    if root is None:
        return None
    if root.val == key:
        return root
    if root.val > key:
        return self.searchBST(root.left, key)
    return self.searchBST(root.right, key)
```

Dry run for `root = [4,2,7,1,3]`, `key = 2`: `searchBST(4)` → 4 > 2 → `searchBST(2)` → equal → return node 2.

## Approach 2 — Iterative (alternative)
Same logic with a loop instead of recursion. Space is O(1).

```python
def searchBST(root, val):
    while root and root.val != val:
        root = root.left if val < root.val else root.right
    return root
```

Both approaches make the same comparisons in the same order. The only difference is recursion stack (O(h)) versus a loop (O(1)).

## Full program (`01_search_in_bst.py`)

```python
"""LeetCode 700 - Search in a Binary Search Tree (recursive solution).

Given the root of a BST and a value, return the subtree rooted at the node with that value,
or None if it does not exist.
"""
from tree_utils import TreeNode, build_tree, to_list


class Solution:
    def searchBST(self, root, key):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        if root is None:
            return None
        if root.val == key:
            return root
        if root.val > key:
            return self.searchBST(root.left, key)
        return self.searchBST(root.right, key)


if __name__ == "__main__":
    sol = Solution()
    root = build_tree([4, 2, 7, 1, 3])
    found = sol.searchBST(root, 2)
    print(to_list(found))         # [2, 1, 3]
    print(sol.searchBST(root, 5))  # None
    assert to_list(sol.searchBST(root, 2)) == [2, 1, 3]
    assert sol.searchBST(root, 5) is None
    print("all checks passed")
```
