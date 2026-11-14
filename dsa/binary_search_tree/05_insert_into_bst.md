# 05 — Insert into a Binary Search Tree (LeetCode 701)

**Link:** https://leetcode.com/problems/insert-into-a-binary-search-tree/

## Problem
Given `root` of a BST and `val`, insert `val` so the tree stays a BST. Return the root. Any valid resulting tree is accepted.

Example: `root = [4,2,7,1,3]`, `val = 5` → one valid answer is `[4,2,7,1,3,null,null,null,null,5]` (5 becomes the left child of 7).

## Approach
Insertion is search that ends in a `None`:
- Walk down exactly like search: `val < node.val` → left, else right.
- When the next child is `None`, put the new node there. That is always a leaf, so the BST property holds.

Edge case: empty tree → the new node becomes the root.

## Pattern to remember
> **BST insert = search until you fall off the tree, then attach a leaf.**

## Complexity
- Time: O(h)
- Space: O(1) iterative (O(h) if written recursively)

## Dry run
`root = [4,2,7,1,3]`, `val = 5`

| Step | cur | Compare | Move/Action |
|------|-----|---------|-------------|
| 1 | 4 | 5 > 4 | cur.right is 7 → cur = 7 |
| 2 | 7 | 5 < 7 | cur.left is None → attach `TreeNode(5)` as 7.left, stop |

In-order afterwards: `[1, 2, 3, 4, 5, 7]` — still sorted, so still a BST.

## Common mistakes
- Forgetting the empty-tree case (`root is None`).
- Going the wrong direction on equality. Pick one rule (here: `>=` goes right) and be consistent.
- Trying to restructure the tree — not needed, a leaf insertion is always valid.

## Full program (`05_insert_into_bst.py`)

```python
"""LeetCode 701 - Insert into a Binary Search Tree (iterative solution).

Insert val into the BST and return the root. The new node is always attached as a leaf.
"""
from tree_utils import TreeNode, build_tree, inorder


class Solution:
    def insertIntoBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        if root is None:
            return TreeNode(val)
        temp = root
        while temp is not None:
            if temp.val > val:
                if temp.left is None:
                    temp.left = TreeNode(val)
                    break
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = TreeNode(val)
                    break
                temp = temp.right
        return root


if __name__ == "__main__":
    sol = Solution()
    root = build_tree([4, 2, 7, 1, 3])
    root = sol.insertIntoBST(root, 5)
    print(inorder(root))  # [1, 2, 3, 4, 5, 7]
    assert inorder(root) == [1, 2, 3, 4, 5, 7]

    empty = sol.insertIntoBST(None, 10)
    assert empty.val == 10
    print("all checks passed")
```
