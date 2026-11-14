# 06 — Delete Node in a BST (LeetCode 450)

**Link:** https://leetcode.com/problems/delete-node-in-a-bst/

## Problem
Given `root` and `key`, delete the node with value `key` and return the root of the modified BST. The tree must remain a valid BST.

Example: `root = [5,3,6,2,4,null,7]`, `key = 3` → `[5,4,6,2,null,null,7]`

## Approach
Split into two parts: **find** the node (search), then **remove** it, which depends on how many children it has.

1. **Not found** (`None`) → return `None`/unchanged.
2. **key smaller / larger** → recurse left / right and reattach the returned subtree.
3. **Found, 0 or 1 child** → return the existing child (splice the node out).
4. **Found, 2 children** → replace its value with the **in-order successor** (smallest node in right subtree). Then delete that successor from the right subtree. The successor has no left child, so this deletion is case 3.

Why the successor? It is the smallest value greater than `node.val` — placing it at the node keeps every left value smaller and every right value larger.

## Pattern to remember
> **BST delete = search + splice.** 0/1 child → bypass. 2 children → copy in-order successor, delete successor.

## Complexity
- Time: O(h) (successor search + recursion path)
- Space: O(h) recursion stack

## Dry run
`root = [5,3,6,2,4,null,7]`, `key = 3`

```
        5
      /   \
     3     6
    / \     \
   2   4     7
```

| Call | node | Action |
|------|------|--------|
| 1 | 5 | 3 < 5 → `root.left = deleteNode(3-subtree, 3)` |
| 2 | 3 | key == 3, found. Has both children (2 and 4) |
| 2a | — | succ = right child 4; 4.left is None → succ = 4 |
| 2b | — | `node3.val = 4` (node now holds 4, left=2, right=4-node) |
| 2c | — | `node3.right = deleteNode(4-node, 4)` |
| 3 | 4 (old) | key == 4, found. No left child → return its right (None) |
| 2d | — | node (now value 4).right = None |

Final tree: 5 → left 4 (left 2, right None), right 6 (right 7).
`to_list` = `[5, 4, 6, 2, None, None, 7]`. In-order = `[2, 4, 5, 6, 7]`, still sorted.

## Common mistakes
- Deleting with 2 children by just reconnecting children (breaks ordering).
- Forgetting to reattach the recursion result: `root.left = deleteNode(...)` is required.
- Using the predecessor instead of successor — also valid, but be consistent.
- Not handling `root is None` at the top (key not in tree).

## Full program (`06_delete_node_in_bst.py`)

```python
"""LeetCode 450 - Delete Node in a BST (recursive solution).

Delete the node with value key (if present) and return the root of the updated BST.
"""
from tree_utils import build_tree, inorder, to_list


class Solution:
    def deleteNode(self, root, key):
        """
        :type root: Optional[TreeNode]
        :type key: int
        :rtype: Optional[TreeNode]
        """
        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            curr = root.right
            while curr.left:
                curr = curr.left

            root.val = curr.val
            root.right = self.deleteNode(root.right, curr.val)

        return root


if __name__ == "__main__":
    sol = Solution()
    root = build_tree([5, 3, 6, 2, 4, None, 7])
    root = sol.deleteNode(root, 3)
    print(to_list(root))  # [5, 4, 6, 2, None, None, 7]
    print(inorder(root))  # [2, 4, 5, 6, 7]
    assert inorder(root) == [2, 4, 5, 6, 7]

    assert sol.deleteNode(build_tree([]), 1) is None
    assert sol.deleteNode(build_tree([1]), 1) is None
    print("all checks passed")
```
